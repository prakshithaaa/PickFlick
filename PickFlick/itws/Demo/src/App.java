public static void main (String []args) {
    @SuppressWarnings("resource")
    Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int rev = 0;

        while (n!=0) {
            int a = n%10;
            rev = rev*10+a;
            n/= 10;
        }

        System.out.println(n);
    }
