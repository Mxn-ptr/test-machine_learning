#!/usr/bin/env python3
""" Frequency """
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """ Create a histogram of student scores for a project"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    x = list(range(0, 101, 10))
    plt.title('Project A')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.xticks(x)
    counts, bin_edges = np.histogram(student_grades, bins=x)
    plt.stairs(counts, bin_edges, fill=True, color='black')
    plt.show()
