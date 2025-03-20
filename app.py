from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

model_name = "neuralmagic/DeepSeek-R1-Distill-Qwen-7B-quantized.w8a8"

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit(1)

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
    app.run(host='0.0.0.0', port=8080)
