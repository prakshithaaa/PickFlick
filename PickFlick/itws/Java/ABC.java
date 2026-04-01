import java.util.*;

class Circle {
double radius;
String color;

Circle() {
this.radius=1;
this.color="White";
}

Circle (double radius) {
this.radius=radius;
this.color="White";
}

Circle (double radius, String color) {
this.radius=radius;
this.color=color;
}

double getArea() {
return 3.14 * radius * radius;
}

void displayInfo() {
System.out.printf("Radius: %.1f, Color: %s, Area: %.2f", radius, color, getArea());
}
}

class ABC {
public static void main(String[]args) {
Scanner in= new Scanner(System.in);
int n = in.nextInt();
in.nextLine();

if (n==1) {
circle = new Circle();
}
if (n==2) {
double radius = in.nextDouble();
circle = new Circle(radius); 
}

if (n==3) {
double radius = in.nextDouble();
in.nextline();
String color = in.nextLine();
circle = new Circle(radius, color);
}

circle.displayInfo();
}
}


