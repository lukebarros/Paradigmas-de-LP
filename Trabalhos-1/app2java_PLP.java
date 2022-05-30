public class app2java_PLP {
    public static void main(String[] args){
        long start = System.currentTimeMillis();
        for (int i = 0; i < 1001; i++){
        System.out.println(i);
        }
        long elapsed = System.currentTimeMillis() - start;
        System.out.print("Tempo de execucao: "+ elapsed +" ms");
    }   
}
