#Challenge 1: Letter Index Dictionary
user_word=input("Enter a word: ")
char_dict={}

for index, char in enumerate(user_word):
    if char in char_dict:
        # If character already exists, append the index to its list
        char_dict[char].append(index)
    else:
        # If character is new, create a new key with a list containing the index
        char_dict[char] = [index]
print(char_dict)


# Challenge 2: Affordable Items
# Sample data
items_purchase = {
    "book": "$15",
    "pen": "$3",
    "notebook": "$10",
    "backpack": "$45"
}

wallet = "$20"

wallet_amount = float(wallet.replace("$", ""))

# Step 2: Clean item prices and find affordable items
affordable_items = []

for item, price in items_purchase.items():
    price_amount = float(price.replace("$", ""))
    if price_amount <= wallet_amount:
        affordable_items.append(item)

# Step 3: Sort the list alphabetically
affordable_items.sort()

# Step 4: Output
if not affordable_items:
    print("Nothing")
else:
    print(affordable_items)