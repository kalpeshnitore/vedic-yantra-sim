import numpy as np

def generate_vastu_grid(size=9):
    """९x९ वास्तु पुरुष मंडळ ग्रिड तयार करतो"""
    grid = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            grid[i, j] = (i * size) + j + 1  # १ ते ८१ क्रमांक
    return grid

def generate_yantra_overlay(size=9):
    """श्रीयंत्राचे ९ स्तर ग्रिडशी मॅप करतो (सध्या डमी कोऑर्डिनेट्स)"""
    overlay = np.zeros((size, size), dtype=float)
    # केंद्र = Bindu (उच्च ऊर्जा), बाहेर = कमी ऊर्जा
    cx, cy = size // 2, size // 2
    for i in range(size):
        for j in range(size):
            dist = np.sqrt((i-cx)**2 + (j-cy)**2)
            overlay[i, j] = max(0, 1.0 - (dist / (size/2)))
    return overlay
