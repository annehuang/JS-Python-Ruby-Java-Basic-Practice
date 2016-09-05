package bi;

import java.math.BigInteger;

public class BI {
	
	// pass in the string-representation of a 128-bit integer in hexadecimal
	// output: turns this string into a BigInteger
	// then turns this BigInteger into a byte array of size 17
	public static void convertStrToArr(String hexBigInt){
		BigInteger num = new BigInteger(hexBigInt, 16);
		System.out.println(num);
		byte[] arr = num.toByteArray();
		System.out.println(arr);
		System.out.println(arr.length);
	}
	
}
