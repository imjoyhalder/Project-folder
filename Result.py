
semester = input("""
                        Semester
                        1st 
                        2nd
                        3rd
                        4th
                        5th
                        6th
                        7th
                        8th
                Enter Semester: """)
roll = int(input("Enter your 6 digits roll numbers: "))
def first():
    data = [
            {643606:{"Name":"Tarana Tabasum Muna",
                    "Result":3.40}},
            {643707:{"Name":"MD Munna",
                    "Result":3.93}},
            {643708:{"Name":"Riaj Mahamud",
                    "Result":3.40}},
            {643709:{"Name":"Samiur Rahaman",
                    "Result":3.80}},
            {643710:{"Name":"Mahamudur Rahman",
                    "Result":3.30}},
            {643711:{"Name":"Arnob Modol",
                    "Result":2.98}},
            {643712:{"Name":"Hasib Abdullah",
                    "Result":3.40}},
            {643713:{"Name":"",
                    "Result":3.40}},
            {643714:{"Name":"Nadiya Rahaman",
                    "Result":3.83}},
            {643715:{"Name":"Sadia Akter",
                    "Result":3.75}},
            {643716:{"Name":"Abu Bakar",
                    "Result":3.30}},
            {643717:{"Name":"Meghla Biswash",
                    "Result":3.85}},
            {643718:{"Name":"Sumita Saha",
                    "Result":3.83}},
            {643719:{"Name":"MD. Jahidul Islam",
                    "Result":3.67}},
            {643720:{"Name":"MD. Adnan Zaman",
                    "Result":3.45}},
            {643721:{"Name":"Bulbuli Howlader",
                    "Fail":"One Subject  Pyhsics-1"}},
            {643722:{"Name":"Tanvin Khan Mahi",
                    "Fail":"Practical all Subjects"}},
            {643723:{"Name":"Iahla Imon",
                    "Result":3.80}},
            {643724:{"Name":"Tasmim Sefa",
                    "Result":3.75}},
            {643725:{"Name":"MD. Zihad",
                    "Result":3.37}},
            {643726:{"Name":"Anika Rahaman",
                    "Result":3.60}},
            {643727:{"Name":"Arpon Kumar Biswas",
                    "Result":3.32}},
            {643728:{"Name":"Maruf Hasan sordar",
                    "Fail":"Two subjects (1.Mathematics-1),(2.Physics-2)"}},
            {643729:{"Name":"Sajjad Hossian",
                    "Result":3.70}},
            {643730:{"Name":"Joy Halder",
                    "Result":3.90}},
            {643731:{"Name":"Abubakkar Siddik",
                    "Result":3.32}
        }]
    try: 
        cal = 1
        b = roll-643706
        if roll>643705 and roll<643751:
            cal = cal+b
            a = data[cal-1].values()
            for i in tuple(a):
                p =i.items()
                for j in j:
                        k = str(j)    
                        print(k)
        
        else:
            print(f"Not founded {roll} this roll number")     
    except Exception as e:
        print(e)
if semester == "1st" or semester == "2nd" or semester == "3rd" or semester == "4th" or semester == "5th" or semester == "6th" or semester == "7th" or semester == "8th":

    first()
else: 
    print("Please type right Semester")