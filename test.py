def find2(main,sub,occurrence):
    # Finding nth occurrence of substring
    val = -1
    for i in range(0, occurrence):
        val = main.find(sub, val + 1)
        
    return val

  