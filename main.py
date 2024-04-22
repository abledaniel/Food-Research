import openai
import csv

openai.api_key = ""

def chat_gpt(text):
    response = openai.ChatCompletion.create (
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": text}]
    )
    
    return response.choices[0].message['content'].strip()


def load_data(file):
    food_keeper = []
    with open(file, encoding="utf-8") as tweets:
        food_data = csv.reader(tweets)
        next(food_data)
        for column in food_data:
            food_keeper.append(column[0])
        return food_keeper

# list = load_data("new_test_tweets.csv")
# for row in list:
#     print(row)



if __name__ == "__main__":
    tweets = load_data("new_test_tweets.csv")
    food_result = []
    checked_food_results = []
    input = "\"Output that processes input sentences, identifying food terms while ensuring contextual accuracy and formatting consistency. You should meticulously distinguish between genuine food items, like 'apple' or 'barbecue sauce', and incidental mentions unrelated to food, such as 'pet rabbit'. It must intelligently combine multi-word food phrases into cohesive entities, like 'apple juice' or 'hot sauce', preserving their integrity. You must strictly adhere to guidelines ensuring that only relevant food words are added to the output Python list, without including extraneous terms or the word 'food' itself. Furthermore, it should maintain consistent formatting standards, avoiding the inclusion of unnecessary characters like \"\n\". MAKE SURE ALL TEXT ADDED TO THE LIST IS PART OF THE ORIGINAL SENTENCE If the input sentence contains no food terms, you should return nothing. Otherwise, it should return the identified food words appended to a Python list, formatted appropriately for ease of use and interpretation. Ensure that you interprets the input sentence accurately, captures all pertinent food terms, and outputs them seamlessly, contributing to a streamlined and efficient user experience. ONLY write the results and nothing else make this into a python list so it is formatted correctly. The text will be below use what I wrote to find it.\" "
    num = 0
    for row in tweets:
        word = chat_gpt(input + row)
        food_result.append(word)
        num += 1
        if num == 3:
            break
        input4 = "Find relevant information about each of the food a human to learn what food to cook with it and how to recycle it the result itself it must be very short and brief overall under 25 words for each FOOD make sure it is in PYTHON list DO NOT INCLUDE /n at all"
        input3 = "Examine this Python list closely. Your job is to carefully go through each word and decide if it belongs in the realm of food. Your goal is to remove any words that don't relate to food, leaving only those that are FOOD items not food related so it is edible. REMOVE THE WORDS BUT RETURN IT AS A PYTHON LIST NO OTHER WORDS I NEED IT TO BE FORMATTED CORRECTLY PLEASE SO NO /n."
        # input2 = "Check if this python text is food If it isn't food return a singular word True or False ONLY A SINGULAR WORD. If the list contains ANY words that are not Food say False"
        checked = chat_gpt(input4 + word)
        checked_food_results.append(checked)
    input4 = "Find relevant information about the food itself"
    final_results = []
        
    print("ChatBot Inital Results: ", food_result)
    print("ChatBot Checked Results: ", checked_food_results)
    # print("Final Results: ", final_results)

    
    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() in ["quit"]:
    #         break
    #     food_result.append(chat_gpt(user_input))
    #     response = chat_gpt(user_input)
    #     print("Chatbot: ", response)
            
            