package main.baekjoon;

import java.util.Scanner;

public class Lv1 {

	public static void main(String[] args) {
		
		// https://www.acmicpc.net/problem/2588

		System.out.println("3자리 숫자 곱셈 계산");

		Scanner sc = new Scanner(System.in);
		int A; String B; 
		A = sc.nextInt();
		B = sc.next();
		
		int b3 = Integer.parseInt(B.substring(2));
		int b2 = Integer.parseInt(B.substring(1,2));
		int b1 = Integer.parseInt(B.substring(0,1));
		
		System.out.println(A * b3);
		System.out.println(A * b2 );
		System.out.println(A * b1);
		System.out.println(A * Integer.parseInt(B));  

	}
}
