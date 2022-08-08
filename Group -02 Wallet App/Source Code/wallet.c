#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include<time.h>

int i, j; // Globally declared 
int main_exit; // integer variable declaration

void menu();
struct date //building structure for date
{
    int month, day, year;
};

struct // structure for add/update/remove wallet info and transactions
{

    char name[60];
    int acc_no, age;
    char address[100];
    char citizenship[15];
    double phone;
    char acc_type[10];
    float amt;
    
    struct date dob; // date structure initialization
    struct date deposit; // date structure initialization
    struct date withdraw; // date structure initialization
    
    char category[100];


} add, upd, check, rem, transaction;



void new_acc()  // function for new account 

{
    int choice;
    FILE *ptr;

    ptr = fopen("record.dat", "a+"); // file handling (a+), If the file is opened successfully fopen( ) loads it into memory and sets up a pointer which points to the last character in it. If the file does not exist, a new file is created. Returns NULL, if unable to open file.
wallet_no:
    system("cls");
    printf("\t\t\t\ WALLET ");
    printf("\n\n\nEnter today's date(mm/dd/yyyy):");
    scanf("%d/%d/%d", &add.deposit.month, &add.deposit.day, &add.deposit.year);
    printf("\nEnter the wallet number:");
    scanf("%d", &check.acc_no);
    while (fscanf(ptr, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", &add.acc_no, add.name, &add.dob.month, &add.dob.day, &add.dob.year, &add.age, add.address, add.citizenship, &add.phone, add.acc_type, &add.amt, &add.deposit.month, &add.deposit.day, &add.deposit.year) != EOF)
    {
        if (check.acc_no == add.acc_no) // check if the same wallet number exist
        {
            printf("wallet no. already in use!");
            goto wallet_no;
        }
    }
    add.acc_no = check.acc_no;
    printf("\nEnter the name:");
    scanf("%s", add.name);
    printf("\nEnter the date of birth(mm/dd/yyyy):");
    scanf("%d/%d/%d", &add.dob.month, &add.dob.day, &add.dob.year);
    printf("\nEnter the age:");
    scanf("%d", &add.age);
    printf("\nEnter the address:");
    scanf("%s", add.address);
    printf("\nEnter the citizenship number:");
    scanf("%s", add.citizenship);
    printf("\nEnter the phone number: ");
    scanf("%lf", &add.phone);
    printf("\nEnter the amount to deposit:$");
    scanf("%f", &add.amt);
    printf("\nType of wallet:\n\t#Personal\n\t#Saving\n\t#daily\n\t#Monthly\n\t\n\n\tEnter your choice:");
    scanf("%s", add.acc_type);

    fprintf(ptr, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, add.address, add.citizenship, add.phone, add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);

    fclose(ptr);
    printf("\nwallet created successfully!");
add_invalid:
    printf("\n\n\n\t\tEnter 1 to go to the main menu and 0 to exit:");
    scanf("%d", &main_exit);
    system("cls");
    if (main_exit == 1)
        menu();
    else if (main_exit == 0)
        close();
    else
    {
        printf("\nInvalid!\a");
        goto add_invalid;
    }
}





void edit(void) //edit the wallet info, updating phone and address
{
    int choice, test = 0;
    FILE *old, *newrec;
    old = fopen("record.dat", "r");
    newrec = fopen("new.dat", "w");

    printf("\nEnter the wallet no: ");
    scanf("%d", &upd.acc_no);
    while (fscanf(old, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d", &add.acc_no, add.name, &add.dob.month, &add.dob.day, &add.dob.year, &add.age, add.address, add.citizenship, &add.phone, add.acc_type, &add.amt, &add.deposit.month, &add.deposit.day, &add.deposit.year) != EOF)
    {
        if (add.acc_no == upd.acc_no) // verifying the wallet number
        {
            test = 1;
            printf("\nWhich information do you want to change?\n1.Address\n2.Phone\n\nEnter your choice(1 for address and 2 for phone):");
            scanf("%d", &choice);
            system("cls");
            if (choice == 1)
            {
                printf("Enter the new address:"); //updating address
                scanf("%s", upd.address);
                fprintf(newrec, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, upd.address, add.citizenship, add.phone, add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);
                system("cls");
                printf("Changes saved!");
            }
            else if (choice == 2)
            {
                printf("Enter the new phone number:"); //updating phone
                scanf("%lf", &upd.phone);
                fprintf(newrec, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, add.address, add.citizenship, upd.phone, add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);
                system("cls");
                printf("Changes saved!");
            }
        }
        else
            fprintf(newrec, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, add.address, add.citizenship, add.phone, add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);
    }

    fclose(old);
    fclose(newrec);
    remove("record.dat");
    rename("new.dat", "record.dat"); // renaming the new.dat with record.dat and replacing file

    if (test != 1)
    {
        system("cls");
        printf("\nRecord not found!!\a\a\a");
edit_invalid:
        printf("\nEnter 0 to try again,1 to return to main menu and 2 to exit:");
        scanf("%d", &main_exit);
        system("cls");
        if (main_exit == 1)

            menu();
        else if (main_exit == 2)
            close();
        else if (main_exit == 0)
            edit();
        else
        {
            printf("\nInvalid!\a");
            goto edit_invalid;
        }
    }
    else
    {
        printf("\n\n\nEnter 1 to go to the main menu and 0 to exit:");
        scanf("%d", &main_exit);
        system("cls");
        if (main_exit == 1)
            menu();
        else
            close();
    }
}

void transact(void) // handling transactions
{
    int choice, test = 0;
    FILE *old, *newrec, *tr;
    old = fopen("record.dat", "r");
    newrec = fopen("new.dat", "w");
    tr = fopen("transactions.dat", "a+");
    test = 1;
    fscanf(old,"%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d",&add.acc_no,add.name,&add.dob.month,&add.dob.day,&add.dob.year,&add.age,add.address,add.citizenship,&add.phone,add.acc_type,&add.amt,&add.deposit.month,&add.deposit.day,&add.deposit.year);
    printf("\n\nDo you want to\n1.Deposit\n2.Withdraw?\n\nEnter your choice(1 for deposit and 2 for withdraw):");
    scanf("%d", &choice);
    if (choice == 1)
    {
        printf("Enter the amount you want to deposit:$ "); // deposit(+) with balance
        scanf("%f", &transaction.amt);
        printf("Enter the category where you want to deposit: "); // specifying category
        scanf("%s", &transaction.category);
        add.amt += transaction.amt;
        time_t t;   // not a primitive datatype
        time(&t);
        fprintf(tr, "%0.2f | %s | Deposit | %s\n", transaction.amt, transaction.category, ctime(&t));
        fprintf(newrec, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, add.address, add.citizenship, add.phone, add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);
        printf("\n\nDeposited successfully!");
    }
    else
    {
        printf("Enter the amount you want to withdraw:$ ");//withdraw(-) from balance
        scanf("%f", &transaction.amt);
        printf("Enter the category where you want to withdraw: "); // specifying category
        scanf("%s", transaction.category);
        add.amt -= transaction.amt;
        time_t t;   // not a primitive datatype
        time(&t);
        fprintf(tr, "%0.2lf | %s | Withdraw | %s\n\n", transaction.amt, transaction.category, ctime(&t));
        fprintf(newrec, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, add.address, add.citizenship, add.phone, add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);
        printf("\n\nWithdrawn successfully!");
    }
    fclose(tr);
    fclose(old);
    fclose(newrec);

    remove("record.dat"); //remove old record
    rename("new.dat", "record.dat"); // updating the record
    if (test != 1)
    {
        printf("\n\nRecord not found!!");
transact_invalid:
        printf("\n\n\nEnter 0 to try again,1 to return to main menu and 2 to exit:");
        scanf("%d", &main_exit);
        system("cls");
        if (main_exit == 0)
            transact();
        else if (main_exit == 1)
            menu();
        else if (main_exit == 2)
            close();
        else
        {
            printf("\nInvalid!");
            goto transact_invalid;
        }
    }
    else
    {
        printf("\nEnter 1 to go to the main menu and 0 to exit:");
        scanf("%d", &main_exit);
        system("cls");
        if (main_exit == 1)
            menu();
        else
            close();
    }
}

void see(void)
{
    FILE *ptr;
    int test = 0;
    int choice;
    float time;
    ptr = fopen("record.dat", "r");

    printf("Enter the account number:");
        scanf("%d",&check.acc_no);
        while (fscanf(ptr,"%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d",&add.acc_no,add.name,&add.dob.month,&add.dob.day,&add.dob.year,&add.age,add.address,add.citizenship,&add.phone,add.acc_type,&add.amt,&add.deposit.month,&add.deposit.day,&add.deposit.year)!=EOF)
        {
            if(add.acc_no==check.acc_no)
            {

    system("cls");
    test = 1;

    printf("\nAccount NO.:%d\nName:%s \nDOB:%d/%d/%d \nAge:%d \nAddress:%s \nCitizenship No:%s \nPhone number:%.0lf \nType Of Account:%s \nAmount deposited:$ %.2f \nDate Of Deposit:%d/%d/%d\n\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, add.address, add.citizenship, add.phone,add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);
            }
        }


    fclose(ptr);
    if (test != 1)
    {
        system("cls");
see_invalid:
        printf("\nEnter 0 to try again,1 to return to main menu and 2 to exit:");
        scanf("%d", &main_exit);
        system("cls");
        if (main_exit == 1)
            menu();
        else if (main_exit == 2)
            close();
        else if (main_exit == 0)
            see();
        else
        {
            system("cls");
            printf("\nInvalid!\a");
            goto see_invalid;
        }
    }
    else
    {
        printf("\nEnter 1 to go to the main menu and 0 to exit:");
        scanf("%d", &main_exit);
    }
    if (main_exit == 1)
    {
        system("cls");
        menu();
    }

    else
    {

        system("cls");
        close();
    }
}

void erase(void) //remove wallet
{
    FILE *old, *newrec;
    int test = 0;
    old = fopen("record.dat", "r");
    newrec = fopen("new.dat", "w");
    printf("Enter the account no. of the customer you want to delete:");
    scanf("%d", &rem.acc_no);
    while (fscanf(old, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d", &add.acc_no, add.name, &add.dob.month, &add.dob.day, &add.dob.year, &add.age, add.address, add.citizenship, &add.phone, add.acc_type, &add.amt, &add.deposit.month, &add.deposit.day, &add.deposit.year) != EOF)
    {
        if (add.acc_no != rem.acc_no)
            fprintf(newrec, "%d %s %d/%d/%d %d %s %s %lf %s %f %d/%d/%d\n", add.acc_no, add.name, add.dob.month, add.dob.day, add.dob.year, add.age, add.address, add.citizenship, add.phone, add.acc_type, add.amt, add.deposit.month, add.deposit.day, add.deposit.year);

        else
        {
            test++;
            printf("\nRecord deleted successfully!\n");
        }
    }
    fclose(old);
    fclose(newrec);
    remove("record.dat");
    rename("new.dat", "record.dat");
    if (test == 0)
    {
        printf("\nRecord not found!!\a\a\a");
erase_invalid:
        printf("\nEnter 0 to try again,1 to return to main menu and 2 to exit:");
        scanf("%d", &main_exit);

        if (main_exit == 1)
            menu();
        else if (main_exit == 2)
            close();
        else if (main_exit == 0)
            erase();
        else
        {
            printf("\nInvalid!\a");
            goto erase_invalid;
        }
    }
    else
    {
        printf("\nEnter 1 to go to the main menu and 0 to exit:");
        scanf("%d", &main_exit);
        system("cls");
        if (main_exit == 1)
            menu();
        else
            close();
    }
}

void add_category() //adding category by user
{
    FILE *cat;

    cat = fopen("categories.dat", "a+");
wallet_no:
    system("cls");
    printf("\nEnter category name: ");
    scanf("%s", add.category);

    fprintf(cat, "%s\n", add.category);

    fclose(cat);
    printf("\nCategory created successfully!");
    
    
add_invalid:
    printf("\n\n\n\t\tEnter 1 to go to the main menu and 0 to exit:");
    scanf("%d", &main_exit);
    system("cls");
    if (main_exit == 1)
        menu();
    else if (main_exit == 0)
        close();
    else
    {
        printf("\nInvalid!\a");
        goto add_invalid;
    }
}



void list_transaction() //list of transactions
{
    int test =1;
    FILE * list_trans; //pointer for pointing the transaction file
    char line[121];
    char ** info = NULL;
    int llen;
    int counter = 0;

    int backdown;

    list_trans = fopen("transactions.dat","r");
    printf("Amount | Category | Transaction Type | Date and Time\n");
    while (fgets(line,120,list_trans))
    {

        // Allocate memory for pointer to line just added
        info = realloc(info,(counter+1) * sizeof(char *));
        // And allocate memory for that line itself!
        info[counter] = calloc(sizeof(char),llen+1);
        // Copy the line just read into that memory
        strcpy(info[counter],line);
        counter++;
    }

    for (backdown = counter-1; backdown >= 0; backdown--)
    {
        printf("%s",info[backdown]);
    }


    if (test==0)
    {
        system("cls");
        printf("\nNO RECORDS!!\n");
    }

view_list_invalid:
    printf("\n\nEnter 1 to go to the main menu and 0 to exit:");
    scanf("%d",&main_exit);
    system("cls");
    if (main_exit==1)
        menu();
    else if(main_exit==0)
        close();
    else
    {
        printf("\nInvalid!\a");
        goto view_list_invalid;
    }


}

void menu(void) //main menu
{
    int choice;
    system("cls");
    printf("\n\n\n\n\t\t\t\t\tWALLET APP \n");
    printf("\n\t\t\t\t\tMAIN MENU \n");
    printf("\n\n\t\t 1.Add Wallet Info\n\t\t 2.Check Wallet\n\t\t 3.Update Wallet\n\t\t 4.Remove Wallet\n\t\t 5.Make a Transactions\n\t\t 6.Transaction List\n\t\t 7.Add a new category\n\t\t 8.Exit\n\n\n\n\n\t\t Enter your choice:");
    scanf("%d", &choice);

    system("cls");
    switch (choice) //using switch to take input from user
    {
    case 1:
        new_acc();
        break;
    case 3:
        edit();
        break;
    case 5:
        transact();
        break;
    case 2:
        see();
        break;
    case 4:
        erase();
        break;
    case 7:
        add_category();
        break;
    case 6:
        list_transaction();
        break;
    case 8:
        close();
        break;
    }
}

int main() //main function to execute menu
{
    menu();
    return 0;
}
