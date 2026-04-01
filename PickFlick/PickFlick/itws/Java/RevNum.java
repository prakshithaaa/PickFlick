import java.io.*;
import java.util.*;
class RevNum {
public static void main(String args[]) {
Scanner in = new Scanner(System.in);
System.out.print("Enter the number to be reversed:");
int n=in.nextInt();
int rev=0;

while (n!=0) {
int a=n%10;
rev=rev*10+a;
n/=10;
}

System.out.println("Reversed number: "+rev);
}
}
