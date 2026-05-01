import gradio as gr
from modules.vastu import run_vastu_simulation

def run_sim(subject: str, building: str, direction: str, accuracy: str):
    if subject == "वास्तुशास्त्र":
        return run_vastu_simulation(building, direction, accuracy)
    return None, "⏳ हा विषय लवकरच ॲक्टिव्ह होईल."

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🕉️ श्रीयंत्र ऊर्जा सिम्युलेटर\n*वास्तुशास्त्र मॉड्यूल | हळूहळू इतर विषय जोडले जातील*")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📚 मेनू व सेटिंग्स")
            subject = gr.Dropdown(
                choices=["वास्तुशास्त्र", "ज्योतिषशास्त्र", "आयुर्वेद"],
                value="वास्तुशास्त्र", label="🔹 विषय निवडा"
            )
            building = gr.Dropdown(["निवास", "कार्यालय", "दुकान", "मंदिर"], label="🏢 इमारत प्रकार")
            direction = gr.Dropdown(["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], label="🧭 मुख्य दिशा")
            accuracy = gr.Slider(0.5, 1.0, step=0.1, value=0.8, label="⚙️ अचूकता स्तर")
            run_btn = gr.Button("🚀 सिम्युलेशन चालवा", variant="primary")
            
        with gr.Column(scale=2):
            gr.Markdown("### 🖥️ सिम्युलेशन कॅनव्हस")
            plot_out = gr.Plot()
            text_out = gr.Markdown()
            
    run_btn.click(run_sim, inputs=[subject, building, direction, accuracy], outputs=[plot_out, text_out])

demo.launch()
