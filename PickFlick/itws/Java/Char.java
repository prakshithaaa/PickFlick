import java.io.*;
import java.util.*;
class Char {
public static void main(String args[]) {
Scanner in = new Scanner(System.in);
System.out.print("Enter a character:");

char ch= in.next().charAt(0);

switch (ch) {
case 'a':
case 'e':
case 'i':
case 'o':
case 'u':
System.out.println("Character is a vowel");
break;

default:
System.out.println("Character is a consonant");
break;

}
}
}


