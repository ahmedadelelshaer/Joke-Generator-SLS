import json
import random

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the math book look sad? It had too many problems.",
    "Why did the bicycle fall over? It was two-tired!",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "How does a penguin build its house? Igloos it together.",
    "What did the grape do when it got stepped on? Nothing, it just let out a little wine.",
    "Why was the computer cold? It left its Windows open.",
    "Why did the coffee file a police report? It got mugged.",
    "What’s orange and sounds like a parrot? A carrot.",
    "Why don’t eggs tell jokes? They’d crack each other up.",
    "How do you organize a space party? You planet.",
    "What did the big flower say to the little flower? 'Hey, bud!'",
    "What did the janitor say when he jumped out of the closet? 'Supplies!'",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "What kind of shoes do ninjas wear? Sneakers.",
    "How does a train eat? It goes chew chew.",
    "Why did the cookie go to the doctor? Because it felt crummy.",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "What did the baby corn say to the mama corn? 'Where’s popcorn?'",
    "Why can’t you give Elsa a balloon? Because she’ll let it go.",
    "How does a vampire start a letter? 'Tomb it may concern...'",
    "Why did the stadium get hot after the game? All the fans left.",
    "What lights up a soccer stadium? A soccer match.",
    "Why can’t a nose be 12 inches long? Because then it would be a foot.",
    "What did one wall say to the other wall? 'I’ll meet you at the corner.'",
    "Why couldn’t the leopard play hide and seek? Because he was always spotted.",
    "Why did the scarecrow break up with the field? It was too corny.",
    "How do you make holy water? You boil the hell out of it.",
    "What kind of music do mummies listen to? Wrap music.",
    "Why do cows wear bells? Because their horns don’t work.",
    "What does a cloud wear under its raincoat? Thunderwear.",
    "What do you call cheese that isn’t yours? Nacho cheese.",
    "Why couldn’t the bicycle stand up by itself? It was two-tired.",
    "How does a dog stop a video? By hitting the paws button.",
    "What did the fish say when it hit the wall? 'Dam!'",
    "What’s brown and sticky? A stick.",
    "What did one hat say to the other? 'You stay here, I’ll go on ahead.'",
    "Why are frogs so happy? They eat whatever bugs them.",
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.",
    "Why did the mushroom go to the party alone? Because he’s a fungi.",
    "How do trees access the internet? They log in.",
    "What do you call a pile of cats? A meowtain.",
    "Why don’t koalas count as bears? They don’t have the right koalafications.",
    "What’s a skeleton’s least favorite room in the house? The living room.",
    "How did the barber win the race? He knew all the shortcuts.",
    "Why did the golfer bring an extra pair of pants? In case he got a hole in one."
]


def lambda_handler(event, context):
    joke = random.choice(jokes)
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # Allow any origin
            "Access-Control-Allow-Methods": "GET, OPTIONS",  # Allow GET and OPTIONS methods
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
        },
        "body": json.dumps({"joke": joke})
    }
