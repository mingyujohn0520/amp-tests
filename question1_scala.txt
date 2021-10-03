def howMany(sentence:String): Integer = {

    var sentence_stripped = sentence.replaceAll("""[\p{Punct}&&[^-]]""", "")
    var word_count = 0

    for (element <- sentence_stripped.split(" ") ) {
        println(element.replace(" ",""))
        println(element.replace(" ","").matches("[a-zA-Z\\-]*"))
        if(element.replace(" ","").matches("[a-zA-Z\\-]*") && !element.equals("")) {
            word_count+=1
        }

    }

    return word_count
    

}