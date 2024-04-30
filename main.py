import SMS

threshold = 10

a = []
a.append(["Item", "quantity"])
a.append(["eggs1", 2])
a.append(["eggs2", 9])
a.append(["eggs3", 13])
a.append(["eggs4", 4])
a.append(["eggs5", 10])
notEnoughItems = []
for item in a[1:]:  # Skip the header by starting the loop from the second item in the list
    if item[1] < threshold:
        notEnoughItems.append(item[0])

if len(notEnoughItems) == 0:
    serverResponse = SMS.SendSMS("Nothing to refill.")
else:
    msg = "Some item(s) need to refill. Items are: "
    for item in notEnoughItems: # concat items into a single string
        msg += item + ", "
    serverResponse = SMS.SendSMS(msg[:-2])
print(serverResponse)