print("""========================================
\033[0;30;47m           BMI Caculator                \033[0;37;40m

Press \033[5;30;47mCTRL+C\033[0;37;40m to stop.
========================================
""")
w = 0
h = 0

bmi_set = []

# Category 	BMI (kg/m2)[c] 	BMI Prime[c]
# Underweight (Severe thinness) 	< 16.0 	< 0.64
# Underweight (Moderate thinness) 	16.0 - 16.9 	0.64 - 0.67
# Underweight (Mild thinness) 	17.0 - 18.4 	0.68 - 0.73
# Normal range 	18.5 - 24.9 	0.74 - 0.99
# Overweight (Pre-obese) 	25.0 - 29.9 	1.00 - 1.19
# Obese (Class I) 	30.0 - 34.9 	1.20 - 1.39
# Obese (Class II) 	35.0 - 39.9 	1.40 - 1.59
# Obese (Class III) 	≥ 40.0 	≥ 1.60 

def bmi_level(idx):
    if (idx<16.0): return 0
    if (idx<=16.9): return 1
    if (idx<=18.4): return 2
    if (idx<=24.9): return 3
    if (idx<=29.9): return 4
    if (idx<=34.9): return 5
    if (idx<=39.9): return 6
    return 7

levelMsg = [
    "\033[0;36;40mSevere thinness\033[0;37;40m",
    "\033[0;36;40mModerate thinness\033[0;37;40m",
    "\033[0;36;40mMild thinness\033[0;37;40m",
    "Normal           ",
    "\033[0;33;40mPre-obese        \033[0;37;40m",
    "\033[0;31;40mObese (Class I)  \033[0;37;40m",
    "\033[0;31;40mObese (Class II) \033[0;37;40m",
    "\033[0;31;40mObese (Class III)\033[0;37;40m",
]

try: 
    while True:
        n = str(input('Please input patient ID:'))
        w = float(input('Please input the weight (kg):'))
        if w<=0:
            print("Error: invalid value")
            continue
        h = float(input('Please input the height (cm):'))/100
        if h<=0:
            print("Error: invalid value")
            continue
        print()
        bmi = w/(h**2)
        bmi_set.append({
            "id":n,
            "bmi":bmi,
            "lvl":bmi_level(bmi),
            "height": h,
            "weight": w,
        })

except KeyboardInterrupt:
    print("", end="")

print("""
Results:
========================================""")
for b in bmi_set:
    # print(b)
    print ("id: {}\tbmi:{:.2f}\tLevel: {}\theight: {:.2f}\tweight: {}".format(b["id"], b["bmi"], levelMsg[b["lvl"]], b["height"]*100, b["weight"]))
print("========================================\n")