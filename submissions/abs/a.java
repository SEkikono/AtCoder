import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);

		try {
			int result = (int) br.readLine().chars()
			.filter(c -> c=='1')
			.count();
			System.out.println(result);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
