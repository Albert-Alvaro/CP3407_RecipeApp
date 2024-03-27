from openai import OpenAI

# to locate the server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
class LLM:
    def main():
        fridge_contents = []

        exit_keywords = ['done', 'exit', 'quit']
        while True:
            ingredient = input("Enter an ingredient you have in the fridge (or type 'done' to finish): ").strip().lower()
            
            if ingredient in exit_keywords:
                print("Exiting input mode...")
                break
            
            if ingredient in fridge_contents:
                print(f"You already have {ingredient} in the fridge!")
            else:
                fridge_contents.append(ingredient)
                print(f"{ingredient.capitalize()} added to the fridge!")

        print("\nIngredients in the fridge:")
        for ingredient in fridge_contents:
            print("- " + ingredient)

        recipe = LLM.generate_recipe(fridge_contents)

        print("Here is a suggested recipe: ")
        print(recipe)

    def generate_recipe(Ingredient):
        prompt = f'Given the ingredients {", ".join(Ingredient)}, generate a recipe and keep it brief.'
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt}
                ],

            model="local-model",

            temperature=0.7
            )
        

        return completion.choices[0].message.content


if __name__ == "__main__":
    LLM.main()