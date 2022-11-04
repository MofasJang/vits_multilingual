from distutils.command.config import config
import time
import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
import json
import math
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader

import commons
import utils
from data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence

from scipy.io.wavfile import write


def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm
def synthesize(texts,config_path,checkpoint_path,speaker=None):
    hps = utils.get_hparams_from_file(config_path)
    net_g = SynthesizerTrn(
        len(symbols),
        hps.data.filter_length // 2 + 1,
        hps.train.segment_size // hps.data.hop_length,
        n_speakers=hps.data.n_speakers,
        **hps.model).cuda()
    _ = net_g.eval()

    _ = utils.load_checkpoint(checkpoint_path, net_g, None)
    start=time.time()
    for text in texts:
        stn_tst = get_text(text, hps)
        with torch.no_grad():
            x_tst = stn_tst.cuda().unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
            audio = net_g.infer(x_tst, x_tst_lengths, sid=speaker,noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][0,0].data.cpu().float().numpy()
        wavfile.write(os.path.join("sample", "{}.wav".format(text)), hps.data.sampling_rate, audio)
    print(time.time()-start)
        
if __name__=="__main__":
    texts=["[ZH]英伟达开源的自然语音处理开发套件[ZH] [EN]from the standpoint of the good of the industries themselves, as well as the general public interest[EN]"]
    config_path="./configs/baker_ljs_ms.json"
    checkpoint_path="./logs/baker_ljs_ms/G_310000.pth"
    synthesize(texts,config_path,checkpoint_path)
    # texts=["英伟达开源的自然语音处理开发套件 from the standpoint of the good of the industries themselves, as well as the general public interest",
    #     # "from the standpoint of the good of the industries themselves, as well as the general public interest,",
    #     # "secret service agents formed a cordon to keep the press and photographers from impeding their passage and scanned the crowd for threatening movements.",
    #     # "especially as no more time is occupied, or cost incurred, in casting, setting, or printing beautiful letters",
    #     # "the uncle claimed her. the husband resisted.",
    #     # "they bought their offices from one another, and were thus considered to have a vested interest in them.",
    #     # "in the center of the chapel was the condemned pew, a large dock-like erection painted black.",
    #     # "again, a turnkey deposed that his chief did not enter the wards more than once a fortnight.",
    #     # "while neglecting to maintain his unity of ideal in the case of nearly all the numerous species of snakes, he should have added a tiny rudiment in the case of the python",
    #     # "the department hopes to design a practical system which will fully meet the needs of the protective research section of the secret service.",
    #     ]
    # config_path="./configs/baker_ljs.json"
    # checkpoint_path="./logs/baker_ljs/G_92000.pth"
    # synthesize(texts,config_path,checkpoint_path)