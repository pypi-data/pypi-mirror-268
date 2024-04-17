def slip1():
    	print("""1.public class S1Q1 extends Thread 
          	{ 
            	public void run() 
            	{ 
                try 
                { 
                for(char c = 'A'; c <= 'Z'; c++) 
                { 
                System.out.println("Generated Charachter: " + c);
                Thread.sleep(2000); 
                } 
                } 
                catch(InterruptedException e) 
                { 
                System.out.println(e); 
                } 
            	} 
            	public static void main(String args[]) 
            	{ 
                S1Q1 t1 = new S1Q1(); 
                t1.start(); 
            	} 
        	}
        	2.import java.sql.*;
		import java.awt.*;
		import javax.swing.*;
		import java.awt.event.*;
		import javax.swing.table.DefaultTableModel;
		public class S1Q2 extends JFrame implements
		ActionListener {
		JLabel enoLabel, enameLabel, designationLabel,
		salaryLabel;
		JTextField enoField, enameField,
		designationField, salaryField;
		JButton saveBtn, displayBtn;
		JPanel panel, displayPanel;
		public S1Q2() {
		setTitle("Employee Detail Form");
		panel = new JPanel(new GridLayout(5,2));
		displayPanel = new JPanel(new
		BorderLayout());
		enoLabel = new JLabel("Employee Number:");
		panel.add(enoLabel);
		enoField = new JTextField(20);
		panel.add(enoField);
		enameLabel = new JLabel("Employee Name:");
		panel.add(enameLabel);
		enameField = new JTextField(20);
		panel.add(enameField);
		designationLabel = new JLabel("Employee Designation:");
		panel.add(designationLabel);
		designationField = new JTextField(20);
		panel.add(designationField);
		salaryLabel = new JLabel("Employee Salary:");
		panel.add(salaryLabel);
		salaryField = new JTextField(20);
		panel.add(salaryField);
		saveBtn = new JButton("Save Details");
		saveBtn.addActionListener(this);
		panel.add(saveBtn);
		displayBtn = new JButton("Display Details");
		displayBtn.addActionListener(this);
		panel.add(displayBtn);
		add(panel, BorderLayout.PAGE_START);
		add(displayPanel, BorderLayout.CENTER);
		setSize(450,300);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		}
		public void actionPerformed(ActionEvent e) {
		if(e.getSource() == saveBtn)
		saveEmployeeDetails();
		else if(e.getSource() == displayBtn)
		displayEmployeeDetails();
		}
		public void saveEmployeeDetails() {
		String strEno = enoField.getText();
		int eno = Integer.parseInt(strEno);
		String ename = enameField.getText();
		String designation =
		designationField.getText();
		String salary = salaryField.getText();
		try {
		Class.forName("org.postgresql.Driver");
		Connection con =
		DriverManager.getConnection("jdbc:postgresql://local
		host:5432/ty92", "ty92", "ty92");
		PreparedStatement ps =
		con.prepareStatement("INSERT INTO Employee (ENO,
		ENAME, DESIGNATION, SALARY) VALUES (?, ?, ?, ?)");
		ps.setInt(1, eno);
		ps.setString(2, ename);
		ps.setString(3, designation);
		ps.setString(4, salary);
		int rowsAffected = ps.executeUpdate();
		if (rowsAffected > 0) {
		JOptionPane.showMessageDialog(this,
		"Employee details saved successfully");
		} else {
		JOptionPane.showMessageDialog(this,
		"Failed to save employee details", "Error:",
		JOptionPane.ERROR_MESSAGE);
		}
		ps.close();
		con.close();
		} catch (ClassNotFoundException |
		SQLException e) {
		System.out.println(e);
		}
		}
		public void displayEmployeeDetails() {
		try {
		Class.forName("org.postgresql.Driver");
		Connection con =
		DriverManager.getConnection("jdbc:postgresql://local
		host:5432/ty92", "ty92", "ty92");
		Statement stmt = con.createStatement();
		ResultSet rs = stmt.executeQuery("SELECT
		* FROM Employee");
		DefaultTableModel model = new
		DefaultTableModel();
		model.addColumn("Employee Number");
		model.addColumn("Employee Name");
		model.addColumn("Employee Designation");
		model.addColumn("Employee Salary");
		while (rs.next()) {
		Object[] row = {
		rs.getInt("ENO"),
		rs.getString("ENAME"),
		rs.getString("DESIGNATION"),
		rs.getString("SALARY")
		};
		model.addRow(row);
		}
		JTable table = new JTable(model);
		JScrollPane scrollPane = new
		JScrollPane(table);
		displayPanel.removeAll();
		displayPanel.add(scrollPane);
		displayPanel.revalidate();
		rs.close();
		stmt.close();
		con.close();
		} catch (ClassNotFoundException |
		SQLException e) {
		System.out.println(e);
		}
		}
		public static void main(String args[]) {
		new S1Q2();
		}
		}
        	""")
def slip2():
    	print("""1.import java.util.*;
			public class S2Q1 {
			public static void main(String args[]) {
			Scanner sc = new Scanner(System.in);
			System.out.print("\nEnter total number of friends: ");
			int n = sc.nextInt();
			sc.nextLine();
			HashSet<String> friendsSet = new
			HashSet<String>();
			for(int i=0; i<n; i++) {
			System.out.print("\nEnter the name of friend " + (i+1) + ": ");
			String name = sc.nextLine();
			friendsSet.add(name);
			}
			ArrayList<String> sortedFriendsList = new
			ArrayList<String>(friendsSet);
			Collections.sort(sortedFriendsList);
			System.out.println("\n- Sorted friend's list-\n");
			for(String friend : sortedFriendsList)
			System.out.println(friend);
			sc.close();
			}
			}
			2.import java.io.*;
			import java.util.*;
			import javax.servlet.*;
			import javax.servlet.http.*;
			public class S2Q2 extends HttpServlet {
			public void doGet(HttpServletRequest request,HttpServletResponse response) throws
			ServletException, IOException {
			response.setContentType("text/html");
			String serverInfo = getServletContext().getServerInfo();
			Collection<? extends ServletRegistration>
			servletRegistrations = getServletContext().getServletRegistrations().values();
			PrintWriter out = response.getWriter();
			out.println("<html>");
			out.println("<head><title>Servlet
			Information</title></head>");
			out.println("<body>");
			out.println("<h2>Server Information:</h2>");
			out.println("<p>Server Software: " +
			serverInfo + "</p>");
			out.println("<h2>Loaded Servlets:</h2>");
			for (ServletRegistration servletRegistration : servletRegistrations) {
			out.println("<p>" +
			servletRegistration.getName() + "</p>");
			}
			out.println("</body>");
			out.println("</html>");
			}
			}
		""")
def slip3():
    	print("""1.<%@ page language="java" contentType="text/html;
charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Patient Details</title>
</head>
<body>
10<h2>Patient Details</h2>
<table border="1">
<tr>
<th>Patient Number</th>
<th>Patient Name</th>
<th>Address</th>
<th>Age</th>
<th>Disease</th>
</tr>
<%
// Sample patient data (replace this with actual
patient data)
String[][] patients = {
{"P001", "John Doe", "123 Main St", "35",
"Fever"},
{"P002", "Jane Smith", "456 Elm St", "42",
"Headache"},
{"P003", "David Johnson", "789 Oak St",
"28", "Allergy"}
};
// Loop through each patient and display their
details in the table
for (String[] patient : patients) {
%>
<tr>
<td><%= patient[0] %></td>
<td><%= patient[1] %></td>
<td><%= patient[2] %></td>
<td><%= patient[3] %></td>
<td><%= patient[4] %></td>
</tr>
11<%
}
%>
</table>
</body>
</html>

2.import java.util.*;
public class S3Q2 {
public static void main(String args[]) {
LinkedList<String> l1 = new
LinkedList<String>();
l1.add("Apple");
l1.add("Banana");
l1.add("Orange");
System.out.println("\nOriginal linked list:
");
System.out.println(l1);
l1.removeFirst();
12System.out.println("\nLinked list after
removing the first element: ");
System.out.println(l1);
System.out.println("\n- Linked list in
reverse order - \n");
ListIterator<String> itr =
l1.listIterator(l1.size());
while(itr.hasPrevious())
System.out.println(itr.previous());
}
    		""")
def slip4():
	print("""1.import java.awt.*;
import java.awt.event.*;

class Slip8_1 extends Frame implements Runnable
{
            Thread t;
            Label l1;
            int f;
            Slip8_1()
            {
                        t=new Thread(this);
                        t.start();
                        setLayout(null);
                        l1=new Label("Hello JAVA");
                        l1.setBounds(100,100,100,40);
                        add(l1);
                        setSize(300,300);
                        setVisible(true);
                        f=0;
            }
            public void run()
            {
                        try
                        {
                                    if(f==0)
                                    {
                                                t.sleep(200);
                                                l1.setText("");
                                                f=1;
                                    }
                                    if(f==1)
                                    {
                                                t.sleep(200);
                                                l1.setText("Hello Java");
                                                f=0;
                                    }
                        }
                        catch(Exception e)
                        {
                                    System.out.println(e);
                        }
                        run();
            }
            public static void main(String a[])
            {
                        new Slip8_1();
            }
}

2.
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
class Slip16_2 extends JFrame implements ActionListener
{          
            JTextField t1,t2,t3;
            JButton b1,b2,b3;
            JTextArea t;
            JPanel p1,p2;
            Hashtable ts;
            Slip16_2()
            {
                        ts=new Hashtable();
                        t1=new JTextField(10);
                        t2=new JTextField(10);
                        t3=new JTextField(10);
                        b1=new JButton("Add");
                        b2=new JButton("Search");
                        b3=new JButton("Remove");
                        t=new JTextArea(20,20);
                        p1=new JPanel();
                        p1.add(t);
                        p2= new JPanel();
                        p2.setLayout(new GridLayout(2,3));
                        p2.add(t1);
                        p2.add(t2);
                        p2.add(b1);
                        p2.add(t3);
                        p2.add(b2);
                        p2.add(b3);
                        add(p1);
                        add(p2);
                        b1.addActionListener(this);
                        b2.addActionListener(this);
                        b3.addActionListener(this);
                        setLayout(new FlowLayout());
                        setSize(500,500);
                        setVisible(true);
                        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            }
            public void actionPerformed(ActionEvent e)
            {
                        if(b1==e.getSource())
                        {
                                    String name = t1.getText();
                                    int code = Integer.parseInt(t2.getText());
                                    ts.put(name,code);
                                    Enumeration k=ts.keys();
                                    Enumeration v=ts.elements();
                                    String msg="";
                                    while(k.hasMoreElements())
                                    {
                                                msg=msg+k.nextElement()+" = "+v.nextElement()+"\n";
                                    }
                                    t.setText(msg);
                                    t1.setText("");
                                    t2.setText("");
                        }
                        else if(b2==e.getSource())
                        {
                                    String name = t3.getText();

                                    if(ts.containsKey(name))
                                    {
                                                t.setText(ts.get(name).toString());
                                    }

                                    else
                                                JOptionPane.showMessageDialog(null,"City not found ...");
                        }
                        else if(b3==e.getSource())
                        {
                                    String name = t3.getText();

                                    if(ts.containsKey(name))
                                    {
                                                ts.remove(name);
                                                JOptionPane.showMessageDialog(null,"City Deleted ...");
                                    }

                                    else
                                                JOptionPane.showMessageDialog(null,"City not found ...");
                        }
            }
            public static void main(String a[])
            {
                        new Slip16_2();
            }
}

    		""")
def slip7():
    	print("""import java.util.Random;
class NumberGenerator extends Thread {
Random random = new Random();
NumberProcessor processor;
public NumberGenerator(NumberProcessor processor) {
this.processor = processor;
}
public void run() {
while(true) {
int num = random.nextInt(100);
processor.processNumber(num);
try {
Thread.sleep(1000);
} catch (InterruptedException e) {
System.out.println(e);
}
}
}
}
class NumberProcessor {
public synchronized void processNumber(int num)
{
if(num % 2 == 0)
new SquareCalculator(num).start();
else
new CubeCalculator(num).start();
}
}
class SquareCalculator extends Thread {
int num;
public SquareCalculator(int num) {
this.num = num;
}
public void run() {
System.out.println("\nSquare of " + num + "
is " + (num * num));
}
}
class CubeCalculator extends Thread {
int num;
public CubeCalculator(int num) {
this.num = num;
}
public void run() {
System.out.println("\nCube of " + num + " is " + (num * num * num));
}
}
public class S7Q1 {
public static void main(String args[]) {
NumberProcessor processor = new
NumberProcessor();
new NumberGenerator(processor).start();
}
}

2.import java.sql.*;
15public class S7Q2 {
public static void main(String args[]) {
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
Statement stmt = con.createStatement();
stmt.execute("CREATE TABLE IF NOT EXISTS Product(PID int primary key, PNAME varchar(20),PRICE int)");
System.out.println("Table created successfully!");
insertRecords(stmt);
displayRecords(stmt);
stmt.close();
} catch (SQLException |
ClassNotFoundException e) {
System.out.println(e);
}
}
private static void insertRecords(Statement stmt) throws SQLException {
String insertSQL = "INSERT INTO Product(PID, PNAME, PRICE) VALUES ";
String records[] = {"(1, 'A', 12)","(2, 'B', 32)","(3, 'C', 24)","(4, 'D', 14)","(5, 'E',10)"};
for(String record : records)
stmt.executeUpdate(insertSQL + record);
System.out.println("\nRecords inserted into product table successfully!");
}
private static void displayRecords(Statement stmt) throws SQLException {
ResultSet rs = stmt.executeQuery("SELECT * FROM Product");
System.out.println("\n- Records from Product Table -\n");
System.out.println("\nPID\tPNAME\tPRICE");
while(rs.next()) {
int pid = rs.getInt("PID");
String pname = rs.getString("PNAME");
int price = rs.getInt("PRICE");
System.out.println(pid + "\t" + pname + "\t" + price);
}
rs.close();
}
}
    		""")
def slip8():
    	print("""1.import java.io.*;
class ThreadDemo extends Thread {
String msg;
int n;
ThreadDemo(String msg, int n) {
this.msg = msg;
this.n = n;
}
public void run() {
for (int i = 0; i < n; i++) {
System.out.println(msg + ": " + (i+1));
}
}
}
class A1 {
public static void main(String args[]) throwsIOException {
ThreadDemo t1 = new ThreadDemo("Thread1 -> COVID19", 10);
ThreadDemo t2 = new ThreadDemo("Thread2 -> LOCKDOWN2020", 20);
ThreadDemo t3 = new ThreadDemo("Thread3 -> VACCINATED21", 30);
t1.start();
t2.start();
t3.start();
}
}

2.<%@ page language="java" contentType="text/html;
charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<title>Prime Number Checker</title>
</head>
<body>
<h1>Prime Number Checker</h1>
<!-- HTML form to enter the number -->
<form action="" method="get">
Enter a number: <input type="text" name="number">
<input type="submit" value="Check">
</form>
<%!
boolean isPrime(int num) {
if (num <= 1) {
return false;
}
for (int i = 2; i <= Math.sqrt(num);
i++) {
if (num % i == 0) {
return false;
}
}
return true;
}
%>
<%-- Java code to check if the number is prime -
-%>
<%
String numberStr = request.getParameter("number");
if (numberStr != null && !numberStr.isEmpty()) {
int number = Integer.parseInt(numberStr);
boolean isPrimeNumber = isPrime(number);
if (isPrimeNumber) {
%>
<p style="color: red;"><%= number %> is a prime number.</p>
<%
} else {
%>
<p style="color: red;"><%= number %> is not a prime number.</p>
<%
}
} else if (numberStr != null && numberStr.isEmpty()) {
%>
<p style="color: red;">Please enter a number.</p>
<%
}
%>
</body>
</html>
    		""")
def slip11():
	print("""1. 
//Html

<!DOCTYPE html>
<html>
<head>
<title>Search Customer</title>
</head>
<body>
<h1>Search Customer</h1>
<form action="SearchServlet" method="post">
<label for="customerNum">Enter customer
number:</label>
<input type="number" id="customerNum"
name="customerNum" required>
<button type="submit">Search</button>
</form>
</body>
</html>  
 
//search servlet.java

import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class SearchServlet extends HttpServlet {
public void doPost(HttpServletRequest req,HttpServletResponse res) throws IOException, ServletException {
res.setContentType("text/html");
PrintWriter out = res.getWriter();
String custNum = req.getParameter("customerNum");
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92", "ty92", "ty92");
String sql = "SELECT * FROM customer WHERE cust_num = ?";
PreparedStatement pstmt = con.prepareStatement(sql);
pstmt.setString(1, custNum);
ResultSet rs = pstmt.executeQuery();
out.println("<!DOCTYPE html>");
out.println("<html>");
out.println("<head>");
out.println("<title>Search
Customer</title>");
out.println("</head>");
out.println("<body>");
out.println("<h1>Search Customer</h1>");
if(rs.next()) {
String custName = rs.getString("cust_name");
String custAddr = rs.getString("cust_addr");
out.println("<h2>Customer Details</h2>");
out.println("<p>Customer Number: " + custNum + "</p>");
out.println("<p>Customer Name: " + custName + "</p>");
out.println("<p>Customer Address: " + custAddr + "</p>");
} else {
out.println("<p>Error: Customer not found</p>");
}
out.println("</body>");
out.println("</html>");
rs.close();
pstmt.close();
con.close();
} catch (SQLException |
ClassNotFoundException e) {
out.println(e);
}
out.close();
}
}

2.import java.sql.*;
public class S11Q2 {
public static void main(String args[]) {
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM Donor");
ResultSetMetaData rsmd = rs.getMetaData();
int columnCount = rsmd.getColumnCount();
System.out.println("\n- Columns in the DONOR table -\n");
System.out.println("--------------------------------------------");
for(int i=1; i<=columnCount; i++) {
System.out.println("Column Name: " + rsmd.getColumnName(i));
System.out.println("Data Type: " + rsmd.getColumnTypeName(i));
System.out.println("Column Size: " + rsmd.getColumnDisplaySize(i));
System.out.println("--------------------------------------------");
}
rs.close();
stmt.close();
con.close();
} catch (SQLException |
ClassNotFoundException e) {
System.out.println(e);
}
}
}
    		""")
def slip12():
	print("""1.Index.html file:

<!DOCTYPE html>
<html>
<head>
<title>PERFECT NUMBER</title>
</head>
<body>
<form action="perfect.jsp" method="post">
Enter Number :<input type="text" name="num">
<input type="submit" value="Submit" name="s1">
</form>
</body>
</html>

Perfect.jsp file:

<%@ page import="java.util.*" %>
<%
if(request.getParameter("s1")!=null)
{
Integer num,a,i,sum = 0;
num = Integer.parseInt(request.getParameter("num"));
a = num;
for(i=1;i<a;i++)
{
if(a%i==0)
{
sum=sum + i;
}
}
if(sum==a)
{
out.println(+num+ "is a perfect number");
}
else
{
out.println(+num+ "is not a perfect number");
}
} 
%>

2.import java.sql.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
class Slip13_2 extends JFrame implements ActionListener
{          
            JLabel l1,l2,l3;
            JTextField t1,t2,t3;
            JButton b1,b2,b3;
            String sql;
            JPanel p,p1;
            Connection con;
            PreparedStatement ps;
            JTable t;
            JScrollPane js;
            Statement stmt ;
            ResultSet rs ;
            ResultSetMetaData rsmd ;
            int columns;
            Vector columnNames = new Vector();
            Vector data = new Vector();
            Slip13_2()
            {
                        l1 = new JLabel("Enter no :");
                        l2 = new JLabel("Enter name :");
                        l3 = new JLabel("percentage :");       
                        t1 = new JTextField(20);
                        t2 = new JTextField(20);
                        t3 = new JTextField(20);
                        b1 = new JButton("Save");
                        b2 = new JButton("Display");
                        b3 = new JButton("Clear");
                        b1.addActionListener(this);
                        b2.addActionListener(this);
                        b3.addActionListener(this);
                        p=new JPanel();
                        p1=new JPanel();
                        p.add(l1);
                        p.add(t1);
                        p.add(l2);
                        p.add(t2);
                        p.add(l3);
                        p.add(t3);
                        p.add(b1);
                        p.add(b2);
                        p.add(b3);
                        add(p);
                        setLayout(new GridLayout(2,1));
                        setSize(600,800);
                        setVisible(true);
                        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            }
            public void actionPerformed(ActionEvent e)
            {
                        if((JButton)b1==e.getSource())
                        {
                                    int no = Integer.parseInt(t1.getText());
                                    String name = t2.getText();
                                    int p = Integer.parseInt(t3.getText());
                                    System.out.println("Accept Values");
                                    try
                                    {
                                                Class.forName(“org.postgresql.Driver”);
con=DriverManager.getConnection(“jdbc:postgresql://192.168.100.254/Bill”,”oracle”,”oracle”);                                               
sql = "insert into stud values(?,?,?)";
                                                ps = con.prepareStatement(sql);
                                                ps.setInt(1,no);
                                                ps.setString(2, name);
                                                ps.setInt(3,p);
                                                System.out.println("values set");
                                                int n=ps.executeUpdate();
                                                if(n!=0)
                                                {
                                                            JOptionPane.showMessageDialog(null,"Record insered ...");                                  
                                                }

                                                else
                                                            JOptionPane.showMessageDialog(null,"Record NOT inserted ");

                                    }//end of try
                                    catch(Exception ex)
                                    {
                                                System.out.println(ex);          
                                                //ex.printStackTrace();
                                    }

                        }
                        else if((JButton)b2==e.getSource())
                        {
                                    try
                                    {
                                                Class.forName(“org.postgresql.Driver”);
con=DriverManager.getConnection(“jdbc:postgresql://192.168.41.1/Bill”,”ty212”,”ty212”);
                                                System.out.println("Connected");
                                                stmt=con.createStatement();
                                                rs = stmt.executeQuery("select * from stud");
                                                rsmd = rs.getMetaData();
                                                columns = rsmd.getColumnCount();
                                                for(int i = 1; i <= columns; i++)
                                                {
                                                            columnNames.addElement(rsmd.getColumnName(i));
                                                }
                                                while(rs.next())
                                                {
                                                            Vector row = new Vector(columns);
                                                            for(int i = 1; i <= columns; i++)
                                                            {
                                                                        row.addElement(rs.getObject(i));
                                                            }
                                                            data.addElement(row);
                                                }
                                                t = new JTable(data, columnNames);
                                                js = new JScrollPane(t);
                                                p1.add(js);
                                                add(p1);
                                                setSize(600, 600);
                                                setVisible(true);
                                    }
                                    catch(Exception e1)
                                    {
                                                System.out.println(e1);
                                    }
                        }
                        else
                        {
                                    t1.setText(" ");
                                    t2.setText(" ");
                                    t3.setText(" ");
                        }
            }
            public static void main(String a[])
            {
                        Slip13_2 ob = new Slip13_2();
            }
}
    		""")
def slip13():
    	print("""1.import java.sql.*;
public class S13Q1 {
public static void main(String args[]) {
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
DatabaseMetaData dbmd = con.getMetaData();
System.out.println("\nDatabase Product Name: " + dbmd.getDatabaseProductName());
System.out.println("Database Product Version: " + dbmd.getDatabaseProductVersion());
System.out.println("Driver Name: " + dbmd.getDriverName());
System.out.println("Driver Version: " + dbmd.getDriverVersion());
System.out.println("\n- Tables in the Database -\n");
ResultSet rs = dbmd.getTables(null,null,null,new String[]{"TABLE"});
while(rs.next())
System.out.println(rs.getString("TABLE_NAME"));
rs.close();
con.close();
} catch (SQLException |
ClassNotFoundException e) {
System.out.println(e);
}
}
}

2.import java.util.Random;
public class S13Q2 {
public static void main(String args[]) {
Thread thread = new
CustomThread("CustomThread");
thread.start();
}
static class CustomThread extends Thread {
public CustomThread(String name) {
super(name);
}
public void run() {
System.out.println(getName() + " is created.");
Random random = new Random();
int sleepTime = random.nextInt(5000);
System.out.println(getName() + " will sleep for " + sleepTime + " milliseconds.");
try {
Thread.sleep(sleepTime);
} catch (InterruptedException e) {
System.out.println(e);
}
System.out.println(getName() + " is dead.");
}
}
}
    		""")
def slip15():
    	print("""1.class S15Q1 extends Thread {
public void run() {
System.out.println("\nThread Name: " + getName());
System.out.println("Thread Priority: " + getPriority());
}
public static void main(String args[]) {
S15Q1 thread = new S15Q1();
thread.start();
}
}

2.import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class S15Q2 extends HttpServlet {
public void doGet(HttpServletRequest req,HttpServletResponse res) throws IOException,ServletException {
res.setContentType("text/html");
int visitCount = 0;
Cookie[] cookies = req.getCookies();
if (cookies != null) {
for (Cookie cookie : cookies) {
if(cookie.getName().equals("visitCount")) {
visitCount = Integer.parseInt(cookie.getValue());
break;
}
}
}
PrintWriter out = res.getWriter();
out.println("<html>");
out.println("<body>");
if (visitCount == 0)
out.println("<h1>Welcome! This is your
first visit to the page.</h1>");
else
out.println("<h1>Welcome back! You've visited this page " + visitCount + " times.</h1>");
visitCount++;
Cookie visitCookie = new Cookie("visitCount", String.valueOf(visitCount));
res.addCookie(visitCookie);
out.println("<form method=\"post\">");
out.println("<input type=\"submit\" value=\"Refresh\">");
out.println("</form>");
out.println("</body>");
out.println("</html>");
}
public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException {
doGet(req, res);
}
}
    		""")
def slip16():
    	print("""1.import java.util.*;
public class S16Q1 {
public static void main(String args[]) {
Scanner sc = new Scanner(System.in);
TreeSet<String> colors = new TreeSet<>();
System.out.print("\nEnter the number of colors: ");
int n = sc.nextInt();
sc.nextLine();
for(int i=0; i<n; i++) {
System.out.print("Enter color " + (i+1) + ": ");
colors.add(sc.nextLine());
}
System.out.println("\nTreeSet in ascending order is: " + colors);
sc.close();
}
}

2.import java.sql.*;
public class S16Q2 {
public static void main(String args[]) {
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
Statement stmt = con.createStatement();
PreparedStatement pstmt = null;
stmt.executeUpdate("CREATE TABLE IF NOT EXISTS Teacher (TNO int primary key, TNAME varchar(20), SUBJECT varchar(20))");
System.out.println("Table exists /created!");
System.out.println("Inserting values into the table...");
pstmt = con.prepareStatement("INSERT INTO Teacher(TNO,TNAME,SUBJECT) VALUES (?,?,?)");
insertTeacher(pstmt, 101, "Taskar", "JAVA");
insertTeacher(pstmt, 102, "Mahale", "DSA");
insertTeacher(pstmt, 103, "Deore", "C");
insertTeacher(pstmt, 104, "Patil", "CN");
insertTeacher(pstmt, 105, "Kapse", "OS");
System.out.println("\nRecords inserted successfully!");
System.out.println("\nDisplaying details of teachers teaching 'JAVA' subject...");
pstmt = con.prepareStatement("SELECT * FROM Teacher WHERE SUBJECT = ?");
pstmt.setString(1,"JAVA");
ResultSet rs = pstmt.executeQuery();
while(rs.next()) {
int tno = rs.getInt("TNO");
String tname = rs.getString("TNAME");
String sub = rs.getString("SUBJECT");
System.out.println("\nTeacher No.: " + tno);
System.out.println("Teacher Name: " + tname);
System.out.println("Subject: " + sub);
}
rs.close();
pstmt.close();
con.close();
} catch (SQLException | ClassNotFoundException e) {
System.out.println(e);
}
}
private static void
insertTeacher(PreparedStatement pstmt, int tno, String tname, String sub) throws SQLException {
pstmt.setInt(1, tno);
pstmt.setString(2, tname);
pstmt.setString(3, sub);
pstmt.executeUpdate();
}
}
    		""")
def slip17():
    	print("""1.import java.util.*;
import java.io.*;

class Slip19_2
{
            public static void main(String[] args) throws Exception
            {
                        int no,element,i;
                                    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
                                    TreeSet ts=new TreeSet();
                                    System.out.println("Enter the of elements :");
                                    no=Integer.parseInt(br.readLine());
                                    for(i=0;i<no;i++)
                                    {
                                                System.out.println("Enter the element : ");
                                                            element=Integer.parseInt(br.readLine());
                                                            ts.add(element);
                                    }
                       
                                    System.out.println("The elements in sorted order :"+ts);       
                        System.out.println("Enter element to be serach : ");
                        element = Integer.parseInt(br.readLine());
                        if(ts.contains(element))
                                    System.out.println("Element is found");
                        else
                                    System.out.println("Element is NOT found");
            }
}
    		
2.import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
public class S17Q2 extends JFrame {
JTextField textField;
JButton startBtn;
public S17Q2() {
setTitle("Number Display");
setSize(450,300);
setDefaultCloseOperation(EXIT_ON_CLOSE);
setLayout(new FlowLayout());
textField = new JTextField(10);
add(textField);
startBtn = new JButton("Start");
startBtn.addActionListener(new ActionListener() {
public void actionPerformed(ActionEvent e) {
startDisplay();
}
});
add(startBtn);
setVisible(true);
}
private void startDisplay() {
Thread displayThread = new Thread(new DisplayRunnable());
displayThread.start();
}
private class DisplayRunnable implements Runnable {
public void run() {
for(int i=1; i<=100; i++) {
textField.setText(Integer.toString(i));
try {
Thread.sleep(100);
} catch (InterruptedException e) {
System.out.println(e);
}
}
textField.setText("");
}
}
public static void main(String args[]) {
new S17Q2();
}
}
    		""")
def slip18():
    	print("""1.lass S18Q1 extends Thread {
public void run() {
System.out.println("\nThread Name: " + getName());
System.out.println("Thread Priority: " + getPriority());
}
public static void main(String args[]) {
S15Q1 thread = new S18Q1();
thread.start();
}
}

2.<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Student Details Form</title>
</head>
<body>
<h2>Enter Student Details</h2>
<form action="S18Q2" method="post">
<label for="seat_no">Seat No:</label>
<input type="text" id="seat_no" name="seat_no" required><br><br>
<label for="name">Name:</label>
<input type="text" id="name" name="name" required><br><br>
<label for="class">Class:</label>
<input type="text" id="class" name="class" required><br><br>
<label for="total_marks">Total Marks:</label>
<input type="text" id="total_marks" name="total_marks" required><br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>

S18Q2.java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class S18Q2 extends HttpServlet {
public void doPost(HttpServletRequest req,
HttpServletResponse res) throws IOException,
ServletException {
res.setContentType("text/html");
PrintWriter out = res.getWriter();
int seatNo = Integer.parseInt(req.getParameter("seat_no"));
String name = req.getParameter("name");
String stu_class= req.getParameter("class");
int totalMarks = Integer.parseInt(req.getParameter("total_marks"));
double perc = (totalMarks / 500.0) * 100;
String grade;
if (perc >= 90) {
grade = "A+";
} else if (perc >= 80) {
grade = "A";
} else if (perc >= 70) {
grade = "B";
} else if (perc >= 60) {
grade = "C";
} else if (perc >= 50) {
grade = "D";
} else {
grade = "Fail!";
}
out.println("<html><head><title>Student
Details</title></head><body>");
out.println("<h2>Student Details</h2>");
out.println("<p>Seat No.: " + seatNo +"</p>");
out.println("<p>Name: " + name + "</p>");
out.println("<p>Class: " + stu_class +"</p>");
out.println("<p>Total Marks: " + totalMarks+ "</p>");
out.println("<p>Percentage: " + perc + "</p>");
out.println("<p>Grade: " + grade + "</p>");
out.println("</body></html>");
out.close();
}
}
    		""")
def slip19():
    	print("""1.import java.util.*;
public class S19Q1 {
public static void main(String args[]) {
Scanner sc = new Scanner(System.in);
System.out.print("\nEnter the number of
integers: ");
int n = sc.nextInt();
LinkedList<Integer> list = new LinkedList<>();
for(int i=0; i<n; i++) {
System.out.print("Enter integer " + (i+1) + ": ");
list.add(sc.nextInt());
}
System.out.println("\nNegative integers from list:-");
for(int num : list) {
if(num < 0) {
System.out.println(num);
}
}
sc.close();
}
}

2.<!DOCTYPE html>
<html>
<head>
<title>Validate User</title>
</head>
<body>
<form action="UserValidation" method="post">
<label for="username">Enter username:</label>
<input type="text" id="username" name="username" required>
<label for="password">Enter password:</label>
<input type="password" id="password" name="password" required>
<input type="submit" value="Submit">
</form>
</body>
</html>

//uservalidtaion.java

import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class UserValidation extends HttpServlet {
public void doPost(HttpServletRequest req,
HttpServletResponse res) throws ServletException,IOException {
String username = req.getParameter("username");
String password = req.getParameter("password");
boolean isValidUser = validateUser(username,password);
res.setContentType("text/html");
PrintWriter out = res.getWriter();
out.println("<html><body>");
if(isValidUser) {
out.println("<h2>Welcome, " + username + "!</h2>");
} else {
out.println("<h2>Invalid username or password!</h2>");
}
out.println("</body></html>");
}
private boolean validateUser(String username,String password) {
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
PreparedStatement pstmt=con.prepareStatement("SELECT * FROM Users WHERE username=? AND password=?");
pstmt.setString(1, username);
pstmt.setString(2, password);
ResultSet rs = pstmt.executeQuery();
if(rs.next())
return true;
rs.close();
pstmt.close();
con.close();
} catch (SQLException | ClassNotFoundException e) {
System.out.println(e);
}
return false;
}
}
    		""")
def slip21():
    	print("""1.import java.util.*;
public class S21Q1 {
public static void main(String args[]) {
Scanner sc = new Scanner(System.in);
LinkedList<String> list = new LinkedList<>();
System.out.print("\nEnter the number of subjects: ");
int n = sc.nextInt();
sc.nextLine();
for(int i=0; i<n; i++) {
System.out.print("Enter subject " + (i+1) + ": ");
list.add(sc.nextLine());
}
System.out.println("\nList items:-");
Iterator<String> itr = list.iterator();
while(itr.hasNext()) {
System.out.println(itr.next());
}
sc.close();
}
}

2.class Buffer {
private String data;
private boolean produced;
Buffer() {
this.data = null;
this.produced = false;
}
public synchronized void produce(String item) throws InterruptedException {
while (produced)
wait();
data = item;
produced = true;
System.out.println("Produced: " + item);
notify();
}
public synchronized String consume() throwsInterruptedException {
while (!produced)
wait();
String consumedItem = data;
produced = false;
System.out.println("Consumed: " + consumedItem);
notify();
return consumedItem;
}
}
class Producer extends Thread {
private String msg;
private Buffer buffer;
private int count;
Producer(String msg, Buffer buffer, int count) {
this.msg = msg;
this.buffer = buffer;
this.count = count;
}
public void run() {
try {
for (int i = 0; i < count; i++) {
buffer.produce(msg);
Thread.sleep(1000);
}
} catch (InterruptedException e) {
System.out.println(e);
}
}
}
class Consumer extends Thread {
private Buffer buffer;
private int count;
Consumer(Buffer buffer, int count) {
this.buffer = buffer;
this.count = count;
}
public void run() {
try {
for (int i = 0; i < count; i++) {
buffer.consume();
Thread.sleep(1000);
}
} catch (InterruptedException e) {
System.out.println(e);
}
}
}
public class S21Q2 {
public static void main(String args[]) {
Buffer buffer = new Buffer();
Producer producer = new Producer("Hello!",buffer, 6);
Consumer consumer = new Consumer(buffer, 6);
producer.start();
consumer.start();
}
}
    		""")
def slip22():
    	print("""1.import java.sql.*;
public class S22Q1 {
public static void main(String[] args) {
Connection conn = null;
Statement stmt = null;
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
stmt = conn.createStatement();
boolean exit = false;
while (!exit) {
System.out.println("\nEmployee Management System");
System.out.println("1. Insert");
System.out.println("2. Update");
System.out.println("3. Display");
System.out.println("4. Exit");
System.out.print("Enter your choice: ");
int choice = Integer.parseInt(System.console().readLine());
54switch (choice) {
case 1:
insertEmployee(stmt);
break;
case 2:
updateEmployee(stmt);
break;
case 3:
displayEmployees(stmt);
break;
case 4:
exit = true;
break;
default: System.out.println("Invalid choice! Please enter a number between 1 and 4.");
}
}
stmt.close();
conn.close();
} catch (SQLException se) {
se.printStackTrace();
} catch (Exception e) {
e.printStackTrace();
} finally {
try {
if (stmt != null) stmt.close();
} catch (SQLException se2) {
}
try {
if (conn != null) conn.close();
} catch (SQLException se) {
se.printStackTrace();
}
}
}
static void insertEmployee(Statement stmt)throws SQLException {
System.out.println("\nInsert Employee");
System.out.print("Enter Employee Number: ");
int eno = Integer.parseInt(System.console().readLine());
System.out.print("Enter Employee Name: ");
String ename = System.console().readLine();
System.out.print("Enter Designation: ");
String designation =
System.console().readLine();
System.out.print("Enter Salary: ");
double salary =
Double.parseDouble(System.console().readLine());
String sql = "INSERT INTO Employee (eno, ename, designation, salary) VALUES (" + eno + ", '"+ ename + "', '" + designation + "', " + salary +
")";
stmt.executeUpdate(sql);
System.out.println("Employee inserted successfully.");
}
static void updateEmployee(Statement stmt)
throws SQLException {
System.out.println("\nUpdate Employee");
System.out.print("Enter Employee Number: ");
int eno = Integer.parseInt(System.console().readLine());
System.out.print("Enter new Salary: ");
double salary = Double.parseDouble(System.console().readLine());
String sql = "UPDATE Employee SET Salary=" + salary + " WHERE eno=" + eno;
int rowsAffected = stmt.executeUpdate(sql);
if (rowsAffected > 0)
System.out.println("Employee updated successfully.");
else
System.out.println("Employee not found.");
}
static void displayEmployees(Statement stmt)
throws SQLException {
System.out.println("\nEmployee List");
String sql = "SELECT * FROM Employee";
ResultSet rs = stmt.executeQuery(sql);
while (rs.next()) {
int eno = rs.getInt("eno");
String ename = rs.getString("ename");
String designation =
rs.getString("designation");
double salary = rs.getDouble("salary");
System.out.println("Employee Number: " + eno + ", Employee Name: " + ename + ", Designation: " + designation + ", Salary: " + salary);
}
rs.close();
}
}

2.<%@ page language="java" contentType="text/html;
charset=UTF-8"
pageEncoding="UTF-8"%>
<%@ page import="pkg.GreetingService" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Greeting</title>
</head>
<body>
<h2>Greeting</h2>
<form action="" method="post">
Enter your name: <input type="text" name="username"><br>
Enter your password: <input type="password"name="password"><br>
<input type="submit" value="Submit">
</form>
<%
request.setCharacterEncoding("UTF-8");
String username = request.getParameter("username");
String password = request.getParameter("password");
if(username != null && !username.isEmpty()
&& password != null && !password.isEmpty()) {
String greeting =
GreetingService.getGreeting(username);
out.println("<p>" + greeting + "</p>");
}
%>
</body>
</html>
    		""")
def slip23():
    	print("""1.import java.util.*;
class VowelThread extends Thread {
private String inputString;
public VowelThread(String inputString) {
this.inputString = inputString;
}
public void run() {
try {
for(int i=0; i<inputString.length(); i++) {
char ch = inputString.charAt(i);
if(isVowel(ch)) {
System.out.println(ch);
Thread.sleep(3000);
}
}
} catch (InterruptedException e) {
System.out.println(e);
}
}
private boolean isVowel(char ch) {
ch = Character.toLowerCase(ch);
return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}
}
public class S23Q1 {
public static void main(String args[]) {
Scanner sc = new Scanner(System.in);
System.out.print("\nEnter a string: ");
String inputString = sc.nextLine();
VowelThread thread = new
VowelThread(inputString);
thread.start();
sc.close();
}
}

2.import java.util.*;
public class S23Q2 {
public static void main(String args[]) {
List<String> studentNames = new ArrayList<>();
for(String arg : args)
studentNames.add(arg);
System.out.println("\nStudent names using Iterator:-");
Iterator<String> itr = studentNames.iterator();
while(itr.hasNext())
System.out.println(itr.next());
System.out.println("\nStudent names using ListIterator:-");
ListIterator<String> listItr = studentNames.listIterator();
while(listItr.hasNext())
System.out.println(listItr.next());
}
}
    		""")	
def slip26():
    	print("""1.import java.sql.*;
public class S26Q1 {
public static void main(String args[]) {
int empId = Integer.parseInt(args[0]);
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
PreparedStatement pstmt = con.prepareStatement("DELETE FROM Employee WHERE eno = ?");
pstmt.setInt(1, empId);
int rowAffected = pstmt.executeUpdate();
if(rowAffected > 0)
System.out.println("\nDetails of employee with ID " + empId + " deleted successfully!");
else
System.out.println("Employee with ID " + empId + " not found.");
} catch(SQLException |
ClassNotFoundException e) {
System.out.println(e);
}
}
}

2.<%@ page language="java" contentType="text/html;
charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Sum of first and last digit</title>
</head>
<body>
<h2>Calculate Sum of First and Last Digits</h2>
<form action="" method="post">
Enter a number: <input type="text" name="number"><br>
<input type="submit" value="Calculate">
</form>
<%
String numberStr = request.getParameter("number");
if(numberStr != null && !numberStr.isEmpty()) {
int number =
Integer.parseInt(numberStr);
int firstDigit = Character.getNumericValue(numberStr.charAt(0));
int lastDigit = number % 10;
int sum = firstDigit + lastDigit;
%>
<p style="color: red; font-size: 18px;">Sum of first and last digit of <%= number %>: <%= sum
%></p>
<% } %>
</body>
</html>
    		""")
def slip27():
    	print("""1.import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.ArrayList;
public class S27Q1 extends JFrame {
public S27Q1() {
setTitle("College Details");
setSize(600, 400);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setLocationRelativeTo(null);
initComponents();
}
private void initComponents() {
ArrayList<College> colleges = new ArrayList<>();
colleges.add(new College(1, "ABC College", "123 Main St", 2000));
colleges.add(new College(2, "XYZ College", "456 Elm St", 1995));
colleges.add(new College(3, "PQR College", "789 Oak St", 2010));
String[] columnNames = {"CID", "CName", "Address", "Year"};
DefaultTableModel model = new DefaultTableModel(columnNames, 0);
for (College college : colleges) {
Object[] rowData = {college.getCID(), college.getCName(), college.getAddress(), college.getYear()};
model.addRow(rowData);
}
JTable table = new JTable(model);
JScrollPane scrollPane = new JScrollPane(table);
getContentPane().add(scrollPane, BorderLayout.CENTER);
}
public static void main(String[] args) {
new S27Q1().setVisible(true);
}
}
class College {
private int CID;
private String CName;
private String address;
private int year;
public College(int CID, String CName, String address, int year) {
this.CID = CID;
this.CName = CName;
69this.address = address;
this.year = year;
}
public int getCID() {
return CID;
}
public String getCName() {
return CName;
}
public String getAddress() {
return address;
}
public int getYear() {
return year;
}
}

2.import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class S27Q2 extends HttpServlet {
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
HttpSession session = request.getSession();
session.setMaxInactiveInterval(300);
response.setContentType("text/html");
PrintWriter out = response.getWriter();
out.println("<html>");
out.println("<head>");
out.println("<title>Session Timeout Interval Changed</title>");
out.println("</head>");
out.println("<body>");
out.println("<h1>Session Timeout Interval
Changed</h1>");
out.println("<p>The inactive time interval of the session has been changed to 5 minutes.</p>");
out.println("</body>");
out.println("</html>");
}
}


    		""")	
def slip28():
    	print("""1.<%@ page language="java" contentType="text/html;
charset=UTF-8"
pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Reverse String</title>
</head>
<body>
<h2>Enter a String:</h2>
<form action="" method="post">
<input type="text" name="inputString">
<input type="submit" value="Reverse">
</form>
<%
String inputString = request.getParameter("inputString");
if (inputString != null && !inputString.isEmpty()) {
StringBuilder reversedString = new StringBuilder(inputString).reverse();
%>
<h2>Reversed String:</h2>
<p><%= reversedString.toString() %></p>
<%
}
%>
</body>
</html>

//S28Q2.java
public class S28Q2 {
public static void main(String[] args) {
Thread thread = new Thread(new
MyRunnable());
thread.start();
System.out.println("Main thread name: " + Thread.currentThread().getName());
}
}
class MyRunnable implements Runnable {
public void run() {
System.out.println("Currently executing
thread name: " + Thread.currentThread().getName());
}
}
    		""")	
def slip29():
    	print("""1.import java.sql.*;
public class S29Q1 {
public static void main(String args[]) {
try {
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM Donor");
ResultSetMetaData rsmd = rs.getMetaData();
for(int i = 1; i <= rsmd.getColumnCount(); i++) {
System.out.println("Column Name: " + rsmd.getColumnName(i));
System.out.println("Data Type: " + rsmd.getColumnTypeName(i));
System.out.println("Column Type: " + rsmd.getColumnType(i));
System.out.println("--------------------------------------------------");
}
} catch (SQLException |
ClassNotFoundException e) {
System.out.println(e);
}
}
}

2.import java.util.*;
public class S29Q2 {
public static void main(String args[]) {
LinkedList<Integer> list = new
LinkedList<>();
list.add(20);
list.add(30);
System.out.println("\nOriginal Liked List: " + list);
list.addFirst(10);
System.out.println("\nLiked List after adding element at first position: " + list);
list.removeLast();
System.out.println("\nLiked List after deleting the last element: " + list);
System.out.println("\nSize of the Linked List: " + list.size());
}
}
    		""")	
def slip30():
	print("""1.import java.io.*;
import java.util.*;
class Sender {
	public void send(String msg)
	{
		System.out.println("Sending\t" + msg);
		try {
			Thread.sleep(1000);
		}
		catch (Exception e) {
			System.out.println("Thread interrupted.");
		}
		System.out.println("\n" + msg + "Sent");
	}
}
class ThreadedSend extends Thread {
	private String msg;
	Sender sender;
	ThreadedSend(String m, Sender obj)
	{
		msg = m;
		sender = obj;
	}
	public void run()
	{
		synchronized (sender)
		{
			sender.send(msg);
		}
	}
}
class SyncDemo {
	public static void main(String args[])
	{
		Sender send = new Sender();
		ThreadedSend S1 = new ThreadedSend(" Hi ", send);
		ThreadedSend S2 = new ThreadedSend(" Bye ", send);
		S1.start();
		S2.start();
		try {
			S1.join();
			S2.join();
		}
		catch (Exception e) {
			System.out.println("Interrupted");
		}
	}
}

2.import java.io.*;
import java.sql.*;
import java.util.*;
class Slip25_2
{
public static void main(String args[])
{
Connection conn= null;
Statement stmt = null;
ResultSet rs = null;
int ch;
Scanner s=new Scanner(System.in);
try
{
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/ty92","ty92","ty92");
stmt = conn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
rs = stmt.executeQuery("select * from employee");
int count=0;
while(rs.next())
count++;
System.out.println("Which Record u want");
System.out.println("Records are = "+count);
do
{ System.out.println("1 First \n2 last \n3 next \n4 prev \n0 Exit");
ch=s.nextInt();
switch(ch)
{
case 1: rs.first();
System.out.println("Roll :"+rs.getInt(1)+" Name :"+rs.getString(2)); break;
case 2: rs.last();
System.out.println("Roll :"+rs.getInt(1)+" Name :"+rs.getString(2)); break;
case 3 : rs.next();
if(rs.isAfterLast())
System.out.println("can't move forword");
else
System.out.println("Roll :"+rs.getInt(1)+" Name :"+rs.getString(2));
break;
case 4 : rs.previous();
if(rs.isBeforeFirst())
System.out.println("can't move backword");
else
System.out.println("Roll :"+rs.getInt(1)+" Name :"+rs.getString(2));
break;
case 0 : break;
default:System.out.println("Enter valid operation");
}
}while(ch!=0);
}
catch(Exception e)
{
System.out.println(e);
}
}
}
    		""")		
