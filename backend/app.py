import gradio as gr

def describe_weather(condition):
    condition = condition.lower()
    descriptions = {
        "sunny": "It's bright and sunny! A perfect day to go outside.",
        "rainy": "It's raining. You might want to carry an umbrella.",
        "cloudy": "The sky is cloudy. It may rain later.",
        "windy": "It's windy. Be careful of strong breeze.",
        "snowy": "It's snowing! Stay warm and enjoy the view."
    }

    return descriptions.get(condition, "Sorry, I don't recognize that weather condition.")

demo = gr.Interface(
    fn=describe_weather,
    inputs="text",
    outputs="text"
)

if __name__ == "__main__":
    demo.launch()
