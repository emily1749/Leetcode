// Collaborative Editor for sharing code!
function example() {
  var message = "Hello, world.";
  console.log(message);
}

https://leetcode.com/problems/goat-latin/


A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

class Solution {
    fun toGoatLatin(input: String): String {
        var words = input.split(' ')

        var newWords = ArrayList<String>(words.size)
        var count = 1

        for (word in words) {
            var newWord = ""
          if(word[0].toLowerCase() in "aeiou") {
                newWord = word
          }
          else {
            newWord = word.substring(1) + word[0]
          }

            newWords.add(newWord + "ma" + "a".repeat(count))
            count++
        }

        var sb = StringBuilder()
        sb.append(newWords[0])
        for (i in 1 until newWords.size) {
          sb.append(" ")
          sb.append(newWords[i])
        }
                      
		return sb.toString()
    }
}



              



// https://leetcode.com/problems/rotate-image/


def rotate_matrix(matrix):
	height = len(matrix)
    width = len(matrix[0])
    
    for i in range(height):
    	for j in range(i, width):
        	matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(height):
    	for j in range(0, int(width*.5)):
        	matrix[i][j], matrix[i][width-j-1] = matrix[i][width-j-1], matrix[i][j]
            
    return matrix
    
    


Input: matrix = 
  
             (0,2)
       [[1,2,3],
 (1,0  [4,5,6],
       [7,8,9]]
   
   
for i in height
	for j in range(i, width)
    	matrix[i][j] = matrix[j][i]
    	
          (0,0)
          [1, 4, 7]
          [2, 5, 8]
 (2, 0)   [3, 6, 9]
  

for i in height
	for j in range(0, .5(width))
    	matrix[i][j] = matrix[i][width-j-1]
        
         (0,2)
   [7, 4, 1]
   [8, 5, 2]
   [9, 6, 3]
   
   
Output: 
[[7,4,1],
 [8,5,2],
 [9,6,3]]
 
 
 
 
 time:O(N) N being how many items are in the matrix
 spaceO(1) constant space