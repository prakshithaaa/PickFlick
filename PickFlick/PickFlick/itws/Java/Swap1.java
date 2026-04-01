import java.io.*;
import java.util.*;
class Swap1 {
public static void main(String args[]) {
Scanner in = new Scanner(System.in);
System.out.print("Enter two numbers:");
int a=in.nextInt();
int b=in.nextInt();
int temp=a;
a=b;
b=temp;
System.out.println("Reversed numbers are:" +a +","+b);


