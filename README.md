# 🕉️ Vedic Yantra Simulator (वैदिक यंत्र सिम्युलेटर)

**Shri Yantra Energy Simulator - Vastu Shastra Module**

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/Gradio-4.0+-orange.svg)](https://gradio.app/)

<div align="center">

**वैदिक विज्ञान + आधुनिक तंत्रज्ञान = ऊर्जा सिम्युलेशन**

*श्रीयंत्राच्या माध्यमातून वास्तुशास्त्र, ज्योतिषशास्त्र, आयुर्वेद यांचा ऊर्जा प्रवाहाचा अभ्यास*

</div>

---

## 📋 विषयसूची (Table of Contents)

- [वैशिष्ट्ये](#-वैशिष्ट्ये-features)
- [इंस्टॉलेशन](#-इंस्टॉलेशन-installation)
- [वापर](#-वापर-usage)
- [प्रोजेक्ट स्ट्रक्चर](#-प्रोजेक्ट-स्ट्रक्चर-project-structure)
- [रोडमॅप](#-रोडमॅप-roadmap)
- [योगदान](#-योगदान-contributing)
- [परवाना](#-परवाना-license)
- [संपर्क](#-संपर्क-contact)

---

## 🌟 वैशिष्ट्ये (Features)

### सध्या उपलब्ध (Currently Available)
- ✅ **वास्तुशास्त्र मॉड्यूल**: ९x९ वास्तु पुरुष मंडळ + श्रीयंत्र ओव्हरले
- ✅ **ऊर्जा प्रवाह व्हिज्युअलायझेशन**: ग्रिड-आधारित ऊर्जा मॅपिंग
- ✅ **सोपा Gradio UI**: Dropdown मेनू + Sidebar फिल्टर्स
- ✅ **रिअल-टाइम सिम्युलेशन**: पॅरामीटर्स बदलून त्वरित निकाल

### लवकरच येत आहे (Coming Soon)
- 🔄 **इमेज-आधारित विश्लेषण**: OpenCV द्वारे जागेचा फोटो अपलोड → वास्तु ग्रिड डिटेक्शन
- 🔄 **ज्योतिषशास्त्र मॉड्यूल**: ग्रहस्थाने → श्रीयंत्र ऊर्जा मॅपिंग
- 🔄 **आयुर्वेद मॉड्यूल**: मर्मा बिंदू + ऊर्जा चिकित्सा
- 🔄 **3D व्हिज्युअलायझेशन**: Blender/Three.js इंटीग्रेशन
- 🔄 **Blogger API**: सिम्युलेशन रिझल्ट्स ऑटो-पोस्टिंग

---

## 📦 इंस्टॉलेशन (Installation)
### पद्धत १: लोकल सेटअप (Local Setup)

```bash
# 1. रिपॉझिटरी क्लोन करा
git clone https://github.com/kalpeshnitore/vedic-yantra-sim.git
cd vedic-yantra-sim

# 2. व्हर्च्युअल एन्व्हायरन्मेंट तयार करा (पर्यायी)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# किंवा
venv\Scripts\activate     # Windows

# 3. आवश्यक लायब्ररीज इन्स्टॉल करा
pip install -r requirements.txt

# 4. ॲप चालवा
python app.py

# 5. ब्राउझरमध्ये उघडा
# http://localhost:7860
```

### पद्धत २: Hugging Face Spaces (लाईव्ह डेमो)

लाईव्ह डेमो येथे उपलब्ध: **[हँगिंग फेस स्पेस लिंक](https://huggingface.co/spaces/kalpeshnitore/vedic-yantra-sim)**

---

## 🎮 वापर (Usage)

### १. वास्तुशास्त्र सिम्युलेशन

1. **विषय निवडा**: Dropdown मधून `वास्तुशास्त्र` निवडा
2. **पॅरामीटर्स सेट करा**:
   - 🏢 **इमारत प्रकार**: निवास / कार्यालय / दुकान / मंदिर
   - 🧭 **मुख्य दिशा**: पूर्व / पश्चिम / उत्तर / दक्षिण
   - ⚙️ **अचूकता स्तर**: 0.5 ते 1.0 (स्लाइडर)
3. **सिम्युलेशन चालवा**: `🚀 सिम्युलेशन चालवा` बटण दाबा
4. **निकाल पहा**:
   - 📊 **ऊर्जा हीटमॅप**: ९x९ ग्रिडवर रंगीत ऊर्जा वितरण
   - 📝 **रिपोर्ट**: सर्वोच्च ऊर्जा केंद्र + शिफारसी

### उदाहरण (Example)

```python
# modules/vastu.py वापरून
from modules.vastu import run_vastu_simulation

fig, report = run_vastu_simulation(    building_type="निवास",
    direction="पूर्व",
    accuracy="0.9"
)
```

---

## 📁 प्रोजेक्ट स्ट्रक्चर (Project Structure) 
