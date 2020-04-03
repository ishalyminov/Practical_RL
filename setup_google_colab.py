#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def download_github_code(path, local_path='.'):
    filename = os.path.join(local_path, path.rsplit("/")[-1])
    os.system("wget https://github.com/yandexdataschool/Practical_RL/raw/coursera/{} -O {}".format(path, filename))


def setup_week1():
    download_github_code("week1_intro/submit.py")
    download_github_code("grading.py", "..")


def setup_week2():
    download_github_code("week2_model_based/submit.py")
    download_github_code("week2_model_based/mdp.py")
    download_github_code("grading.py", "..")


def setup_week3():
    download_github_code("week3_model_free/submit.py")
    download_github_code("week3_model_free/qlearning.py")
    download_github_code("week3/util.py")
    download_github_code("grading.py", "..")


def setup_week4():
    download_github_code("week4_approx/submit.py")
    download_github_code("week4_approx/framebuffer.py")
    download_github_code("week4_approx/replay_buffer.py")
    download_github_code("grading.py", "..")


def setup_week5():
    download_github_code("week5_policy_based/submit.py")
    download_github_code("week5_policy_based/atari_util.py")
    download_github_code("grading.py", "..")


def setup_week6():
    download_github_code("week6_outro/submit.py")
    os.system("mkdir seq2seq")
    download_github_code("week6_outro/seq2seq/basic_model_tf.py", "week6_outro/seq2seq")
    download_github_code("week6_outro/seq2seq/he-pron-wiktionary.txt", "week6_outro/seq2seq")
    download_github_code("week6_outro/seq2seq/main_dataset.txt", "week6_outro/seq2seq")
    download_github_code("week6_outro/seq2seq/submit.py", "week6_outro/seq2seq")
    download_github_code("week6_outro/seq2seq/cov.py", "week6_outro/seq2seq")

