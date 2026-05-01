import numpy as np
import matplotlib.pyplot as plt
from utils.grid_generator import generate_vastu_grid, generate_yantra_overlay

def run_vastu_simulation(building_type: str, direction: str, accuracy: str):
    """वास्तु + श्रीयंत्र ऊर्जा प्रवाह सिम्युलेशन"""
    # १. ग्रिड तयार करा
    vastu_grid = generate_vastu_grid(9)
    yantra_overlay = generate_yantra_overlay(9)
    
    # २. ऊर्जा गणना (डमी लॉजिक, नंतर अल्गोरिदम जोडा)
    energy_map = vastu_grid * yantra_overlay
    if direction == "पूर्व": energy_map[:, 0] *= 1.2  # सूर्योदय प्रभाव
    if building_type == "निवास": energy_map[4, 4] *= 1.5  # केंद्र महत्त्व
    
    # ३. प्लॉट
    fig, ax = plt.subplots(figsize=(6, 6))
    cax = ax.imshow(energy_map, cmap='viridis', interpolation='nearest')
    ax.set_title(f"वास्तुशास्त्र + श्रीयंत्र ऊर्जा मॅप ({building_type})")
    ax.set_xlabel("X (दिशा)")
    ax.set_ylabel("Y (दिशा)")
    plt.colorbar(cax, ax=ax, label="ऊर्जा तीव्रता")
    
    # ४. टेक्स्ट रिपोर्ट
    max_energy_pos = np.unravel_index(np.argmax(energy_map), energy_map.shape)
    report = f"""
    ✅ **विषय:** वास्तुशास्त्र  
    🏢 **इमारत प्रकार:** {building_type}  
    🧭 **मुख्य दिशा:** {direction}  
    🔋 **सर्वोच्च ऊर्जा केंद्र:** Grid[{max_energy_pos[0]}, {max_energy_pos[1]}]  
    ⚠️ **नोट:** सध्या डमी डेटा वापरला आहे. पुढील अपडेटमध्ये OpenCV इमेज प्रोसेसिंग + खरे वास्तु नियम जोडले जातील.
    """
    return fig, report
