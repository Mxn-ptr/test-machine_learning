#!/usr/bin/env python3
""" Frequency """
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """ Create a histogram of student scores for a project"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(0, 110, 10)
    plt.title('Project A')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.ylim(0, 30)
    plt.xlim(0, 100)
    plt.xticks(x)
    plt.hist(student_grades, bins=x, edgecolor='black')
    plt.show()
