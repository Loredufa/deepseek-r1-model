from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

app = Flask(__name__)

# Definir ruta del modelo persistente en OpenShift
model_path = "/mnt/model"
model_name = "neuralmagic/DeepSeek-R1-Distill-Qwen-7B-quantized.w8a8"

# Si el modelo no existe en el volumen persistente, descargarlo
if not os.path.exists(model_path):
    os.makedirs(model_path, exist_ok=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Guardar el modelo en el almacenamiento persistente
    tokenizer.save_pretrained(model_path)
    model.save_pretrained(model_path)
    print(f"Modelo descargado y almacenado en {model_path}")
else:
    # Si el modelo ya está guardado, cargarlo desde el volumen persistente
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    print(f"Modelo cargado desde {model_path}")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_text = data.get("input_text", "")

    if not input_text:
        return jsonify({"error": "input_text es requerido"}), 400

    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs)
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"output_text": output_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)


