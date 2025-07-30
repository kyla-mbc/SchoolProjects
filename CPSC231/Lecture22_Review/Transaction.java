import java.time.LocalDate;
public class Transaction{

    private String m_payee; 
    private Double m_amount; 
    private LocalDate m_date;

    public Transaction(){
        m_payee = "";
        m_amount = 0.0;
        m_date = LocalDate.now();
    }

    public Transaction(String pay, Double amnt){
        m_payee = pay;
        m_amount = amnt;
        m_date = LocalDate.now(); // gets the current date 
    }

    public Transaction (Transaction t){
        m_payee = t.m_payee;
        m_amount = t.m_amount;
        m_date = t.m_date;
    }

    // getters 
    public String getPayee(){
        return m_payee;
    }

    public Double getAmount(){
        return m_amount;
    }

    public LocalDate getDate(){
        return m_date;
    }

    // setters
    public void setPayee(String p){
        m_payee = p;
    }

    public void setPayee(Double a){
        m_amount = a;
    }

    public String toString(){
        String s = "";
        s += "Date: " + m_date + " Payee: " + m_payee + " Amount: " + m_amount + "\n";
        return s;
    }


}