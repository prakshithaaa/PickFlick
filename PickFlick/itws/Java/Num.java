import java.io.*;
import java.util.*;
class Num {
public static void main(String args[]) {
Scanner in = new Scanner(System.in);
System.out.print("Enter a number:");
float n=in.nextFloat();

float sq= n*n;
System.out.printf("Square of %.2f is %.2f\n", n, sq);

int N= (int)n;
int fact=1;
for (int i=1;i<=N;i++)
{
fact*=i;
}

System.out.printf ("Factorial of %.2f is %d", n, fact);
}
}





