# ===*=== Whatsapp Chat Data Analysis ===*===
n = int(input("Enter the number of messages:"))
data = {}
for i in range(n):
    name, message = input().split(':')
    if name in data:
        data[name].append((i,message))
    else:
        data[name] = [(i,message)]
print(data)
while True:
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. Identify the user with the longest average message length")
    print("13. Count how many messages mention a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions asked in the chat")
    print("17. Calculate the reply ratio between two users")
    print("18. Check for deleted messages")
    print("19.Exit")

    user_in = int(input("Enter Your Choice: "))
    #1. Count total number of messages
    if user_in == 1:
        print(f"The count of total messages {n} ")
    #2. Identify unique users in the chat
    elif user_in == 2:
        print(f"The unique users in the chat {set(data.keys())}")
    #3. Count total words in the chat
    elif user_in == 3:
        total_words = 0
        for name in data.keys():
            for idx,msg in data[name]:
                total_words += len(msg.split())
        print(f"The total words in the chat {total_words}")
    #4. Calculate average words per message
    elif user_in == 4:
        total_words = 0
        for name in data:
            for idx, msg in data[name]:
                total_words += len(msg.split())
        print(f"The average words per message {total_words/n} ")
    #5. Find the longest message sent
    elif user_in == 5:
        max_msg = ''
        for name in data:
            for ind, msg in data[name]:
                if len(max_msg) < len(msg):
                    max_msg = msg
                    user = name
        print(f'Longest message: "{user}: {max_msg}"')
    #6. Find the most active user
    elif user_in == 6:
        max_count = 0
        for name in data:
            if max_count < len(data[name]):
                max_count = len(data[name])
                user = name
        print(f"Most active user: {user} {max_count} message2")
    #7. Get message count for a specific user
    elif user_in == 7:
        u_in = input()
        if u_in in data:
            count_msg = len(data[u_in])
            print(f"Messages sent by {u_in}: {count_msg}")
        else:
            print(f"{u_in} not in present in chat")
    #8. Find the most frequently used word by a specific user
    elif user_in == 8:
        u_in = input()
        d ={}
        if u_in in data:
            for ind, msg in data[u_in]:
                for words in msg.split():
                    if words in d:
                        d[words]= d[words]+1
                    else:
                        d[words] = 1
            print(f"Most frequent word used by {u_in}: {max(d, key=d.get)}")
        else:
            print(f"{u_in} not in present in chat")
    #9. Retrieve the first and last message sent by a user
    elif user_in == 9:
        u_in = input()
        if u_in in data:
            print(f'First message by {u_in}: "{u_in}: {data[u_in][0][1]}"')
            print(f'Last message by {u_in}: "{u_in}: {data[u_in][-1][1]}"')
        else:
            print(f"{u_in} not in present in chat")
    #10. Check if a user is present in the chat
    elif user_in == 10:
        u_in = input()
        if u_in in data():
            print(f"User '{u_in}' found in the chat.")
        else:
            print(f"User '{u_in}' not found in the chat.")
    #11. Find commonly repeated words
    elif user_in == 11:
        d = {}
        l = []
        for name in data:
            for ind, msg in data[name]:
                for words in msg.split():
                    if words in d:
                        d[words] = d[words]+1
                    else:
                        d[words] = 1
            for word in d:
                if d[word] >= 2:
                    l.append(word)
        print(f'Common repeated words: {l}')
    #12. Identify the user with the longest average message length
    elif user_in == 12:
        max_avg = 0
        user = ''
        for name in data:
            total_words = 0
            total_msgs = len(data[name])
            for idx, msg in data[name]:
                total_words += len(msg.split())
                avg = total_words / total_msgs
            if avg > max_avg:
                max_avg = avg
                user = name
        print(f"User with longest average message: {user} (avg {max_avg} words)")
    #13. Count how many messages mention a specific user
    elif user_in == 13:
        u_in = input()
        count = 0
        if u_in in data:
            for name in data:
                for idx, msg in data[name]:
                    for word in msg.split():
                        if u_in == word:
                            count += 1
            print(f"Messages mentioning {u_in}: {count}")
        else:
            print(f"User '{u_in}' not found in the chat.")
    #14. Remove duplicate messages
    elif user_in == 14:
        mess = []
        count = 0
        for name in data:
            for idx, msg in data[name]:
                if msg not in mess:
                    mess.append(msg)
                    count += 1
        print(f"Unique messages count: {count}")
    #15. Sort messages alphabetically
    elif user_in == 15:
        sort_msg = []
        for name in data:
            for idx, msg in data[name]:
                sort_msg.append(msg)
        print(f"All messages sorted A-Z: {sorted(sort_msg)}")
    #16. Extract all questions asked in the chat
    elif user_in == 16:
        lis_qus =[]
        for name in data:
            for idx, msg in data[name]:
                if '?' in msg:
                    lis_qus.append(msg)
        print(f"List of messages ending with or containing ?: {lis_qus}")
    #17. Calculate the reply ratio between two users
    elif user_in == 17:
        u_in = input().split('and')
        u1=0
        u2=0
        if u_in in data:
            for name in data[u_in]:
                u1 = len(data[u_in[0]])
                u2 = len(data[u_in[1]])
        print(f"Reply ratio from {u_in[0]} to {u_in[1]}: {u1//u2}")
    #18. Check for deleted messages
    elif user_in == 18:
        cou = 0
        for name in data:
            for idx, msg in data[name]:
                if msg == "This message was deleted":
                    cou += 1
        print(f"Deleted messages found: {cou}")
    #19.Exit
    elif user_in == 19:
        break 