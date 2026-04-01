import java.util.*;

class BankAccount {
    private int accountNumber;
    private String holderName;
    private double balance;
    static String bankName = "XYZ Bank";
    
    BankAccount (int accountNumber, String holderName, double balance) {
        this.accountNumber=  accountNumber;
        this.holderName = holderName;
        this.balance =  balance;
    }
    
    void deposit (double amount) {
        balance += amount;
    }
    
    void withdraw (double amount) {
        if (amount <= balance) {
            balance -= amount;
        }
        else {
        System.out.printf ("Insufficient balance while withdrawing");
        }
    }
    
    void transferFunds (BankAccount target, double amount) {
        if (amount <= balance) {
            balance -= amount;
            target.deposit(amount);
        }
        else {
            System.out.printf ("Insufficient balance while transfering");
        }
    }
    
    void displayBalance() {
        System.out.printf ("%.2f%n", balance);
    }
    
    public int getAccountNumber() {
        return accountNumber;
    }
}

class Main {
    public static void main (String[] args) {
    Scanner in = new Scanner(System.in);
    
    int accountNo1 = in.nextInt();
        in.nextLine();
        String name1 = in.nextLine();
        double balance1 = in.nextDouble();

        int accountNo2 = in.nextInt();
        in.nextLine(); 
        String name2 = in.nextLine();
        double balance2 = in.nextDouble();

        BankAccount account1 = new BankAccount(accountNo1, name1, balance1);
        BankAccount account2 = new BankAccount(accountNo2, name2, balance2);
        
        double depositAmount1 = in.nextDouble();
        account1.deposit(depositAmount1);

        double withdrawAmount2 = in.nextDouble();
        account2.withdraw(withdrawAmount2);
        
        int fromAccount = in.nextInt();
        int toAccount = in.nextInt();
        double transferAmount = in.nextDouble();

        if (fromAccount == account1.getAccountNumber) {
            account1.transferFunds(account2, transferAmount);
        }
        else {
            account2.transferFunds(account1, transferAmount);
        }

        account1.displayBalance();
        account2.displayBalance();
    }
}