import java.io.*;
import java.util.*;
class Table {
public static void main(String args[]) {
Scanner in = new Scanner(System.in);
int n=in.nextInt();
int i,mult;
System.out.println("Mathematical Table for "+n+":");
for (i=1;i<=10;i++)
{
System.out.println(n +"x" +i +"=" +(n*i));
}
}
}



