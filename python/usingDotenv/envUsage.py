from dotenv import set_key, get_key, dotenv_values

print(get_key(".env", "measure"))

dictFromEnv = dotenv_values(".envdict")
print(dictFromEnv["white"])

currentMeasure = get_key(".env", "measure") #current at '.env' file
try:
    currentMeasure = int(currentMeasure) + 1
except ValueError:
    print("detected non compatible value at measure, resetting to 0.")
    currentMeasure = 0 #reset to default

if __name__ == "__main__":
    if isinstance(currentMeasure, int): #found
        print("changing value in .env")
        measureAddition = currentMeasure
        set_key(".env", "measure", str(measureAddition), quote_mode="never")