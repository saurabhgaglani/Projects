import java.io.*;
public class Canceltic
{
public static void func2() throws IOException
 {
  BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
  System.out.println('\f');
  Railway.headingLine();
  Railway.blankLines(1);
  System.out.println("\t\t\t Cancellation Menu");
  Railway.headingLine();
  Railway.blankLines(1); 
  System.out.println("Please Enter Prno.");
  int p = Integer.parseInt(br.readLine());
   Railway.headingLine();
  Railway.blankLines(1);
  int i3=0;
  for (i3=0; i3<25; i3++)
  { if (Railway.prno[i3]==p)
    { double amt=Railway.amount[i3]-(Railway.amount[i3]*10)/100; 
      System.out.println("Ticket booked by :" + Railway.bookperson[i3]);
      System.out.println("Your Ticket has been cancelled");
      System.out.println("Please collect refund of Rs." + amt);
    }
  }
  Railway.headingLine();
  Railway.blankLines(1);
  Railway.pressKey();
  }
 
 public static void func4() throws IOException
 {
  BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
  System.out.println('\f');
  Railway.headingLine();
  Railway.blankLines(1);
  System.out.println("\t\t\t\t UNBOOKED TICKETS");
  Railway.headingLine();
  Railway.blankLines(1);
  int flag4=0,i4=0;
  while (flag4==0)
  {
  System.out.print("Please enter the train number :");
  int tno = Integer.parseInt(br.readLine());
  for (i4=0; i4<=1; i4++)
   {if (Railway.trno[i4]== tno)
    {flag4=1;
     break;
    }
   }
  if (flag4==0)
   continue;
  }
  int ctr4=1;
  while (ctr4<=3)
  {
   char max[]= new char[25];
   if (i4==0 && ctr4==1)
   { System.out.println("CLASS AC : Seat Numbers");
     for (int p1=0;p1<25;p1++)
      max[p1]=Railway.ac1[p1];}
   if (i4==0 && ctr4==2)
    {System.out.println("FIRST CLASS : Seat Numbers");   
     for (int p1=0;p1<25;p1++)
      max[p1]=Railway.F1[p1];}
   if (i4==0 && ctr4==3)
    {System.out.println("SECOND CLASS : Seat Numbers");   
     for (int p1=0;p1<25;p1++)
      max[p1]=Railway.S1[p1];}
  
   if (i4==1 && ctr4==1)
   { System.out.println("CLASS AC : Seat Numbers");
     for (int p1=0;p1<25;p1++)
      max[p1]=Railway.ac2[p1];}
   if (i4==1 && ctr4==2)
    {System.out.println("FIRST CLASS : Seat Numbers");   
     for (int p1=0;p1<25;p1++)
      max[p1]=Railway.F2[p1];}
   if (i4==1 && ctr4==3)
    {System.out.println("SECOND CLASS : Seat Numbers");   
     for (int p1=0;p1<25;p1++)
      max[p1]=Railway.S2[p1];}
   int i5=0,ctr100=1;
   for (i5=0; i5<max.length; i5++)
   {
    if (max[i5]=='U')
    {
     System.out.print((i5+1)+"       ");
     ctr100 =ctr100+1;
      if (ctr100 > 10)
     { System.out.println();
       ctr100=1; }      
    }  
   }
   System.out.println();
   ctr4=ctr4+1;
  }
  Railway.pressKey();
 }
}

  