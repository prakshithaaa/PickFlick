import java.io.*;
import java.util.*;
class Swap2 {
public static void main(String args[]) {
Scanner in = new Scanner(System.in);
System.out.print("Enter two numbers:");
int a=in.nextInt();
int b=in.nextInt();
a=a+b;
b=a-b;
a=a-b;
System.out.println("Reversed numbers are:" +a +"," +b);
}
}
