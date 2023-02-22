import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Solution {
	
	static int H;
	static int W;
	static String graph[][];
	static int tank_x;
	static int tank_y;
	static int command_count; // 명령어 수
	static String[] command_list; // 명령어 리스트
	static String temp;
	static int test_y;
	static int test_x;
	public static void main(String[] args) throws Exception {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		// 테스트 케이스
		for(int t = 1; t <= T; t++) {
			sb.append("#" + t + " ");
			String[] split = br.readLine().split(" ");
			H = Integer.parseInt(split[0]);
			W = Integer.parseInt(split[1]);
			graph = new String[H][W];
			for(int i = 0; i < H; i++) {
				split = br.readLine().split("");
				for(int j = 0; j < W; j++) {
					graph[i][j] = split[j];
					if(graph[i][j].equals("<") || graph[i][j].equals(">") || graph[i][j].equals("^") || graph[i][j].equals("v")) {
						tank_x = i;
						tank_y = j;
					}
					
				}
			}
			command_count = Integer.parseInt(br.readLine());
			command_list = new String[command_count];
			split = br.readLine().split("");
			for(int i = 0; i < command_count; i++) {
				command_list[i] = split[i]; 
			}
			
			for(String command : command_list) {
				// 윗 화살표로 변경(고정적) 후, 해당 방향이 평지(.)일 경우만 이동
				if(command.equals("U")) {
					graph[tank_x][tank_y] = "^";
					
					if(0 <= tank_x-1 && graph[tank_x-1][tank_y].equals(".")) {
						graph[tank_x-1][tank_y] = "^";
						graph[tank_x][tank_y] = ".";
						tank_x = tank_x-1; // 탱크 이동한 좌표
					} 
				} else if(command.equals("D")) {
					graph[tank_x][tank_y] = "v";
					
					if(H > tank_x+1 && graph[tank_x+1][tank_y].equals(".")) {
						graph[tank_x+1][tank_y] = "v";
						graph[tank_x][tank_y] = ".";
						tank_x = tank_x+1; // 탱크 이동한 좌표
					} 
				} else if(command.equals("L")) {
					graph[tank_x][tank_y] = "<";
					
					if(0 <= tank_y-1 && graph[tank_x][tank_y-1].equals(".")) {
						graph[tank_x][tank_y-1] = "<";
						graph[tank_x][tank_y] = ".";
						tank_y = tank_y-1; // 탱크 이동한 좌표
					}
				} else if(command.equals("R")) {
					graph[tank_x][tank_y] = ">";
					
					if(W > tank_y+1 && graph[tank_x][tank_y+1].equals(".")) {
						graph[tank_x][tank_y+1] = ">";
						graph[tank_x][tank_y] = ".";
						tank_y = tank_y+1; // 탱크 이동한 좌표
					}
					
				} else if(command.equals("S")) {
					if(graph[tank_x][tank_y].equals("<")) {
						test_y = tank_y-1;
						while(test_y >= 0) {
							if(graph[tank_x][test_y].equals("*")) {
								graph[tank_x][test_y] = ".";
								break;
							} else if(graph[tank_x][test_y].equals("#")) {
								break;
							} else {
								test_y -= 1;
							}
						}
					} else if(graph[tank_x][tank_y].equals(">")) {
						test_y = tank_y+1;
						while(test_y < W) {
							if(graph[tank_x][test_y].equals("*")) {
								graph[tank_x][test_y] = ".";
								break;
							} else if(graph[tank_x][test_y].equals("#")) {
								break;
							} else {
								test_y += 1;
							}
						}
					} else if(graph[tank_x][tank_y].equals("^")) {
						test_x = tank_x-1;
						while(test_x >= 0) {
							if(graph[test_x][tank_y].equals("*")) {
								graph[test_x][tank_y] = ".";
								break;
							} else if(graph[test_x][tank_y].equals("#")) {
								break;
							} else {
								test_x -= 1;
							}
						}
						
					} else if(graph[tank_x][tank_y].equals("v")) {
						test_x = tank_x+1;
						while(test_x < H) {
							if(graph[test_x][tank_y].equals("*")) {
								graph[test_x][tank_y] = ".";
								break;
							} else if(graph[test_x][tank_y].equals("#")) {
								break;
							} else {
								test_x += 1;
							}
						}
						
					}
					
				}
			}
			
			for(int i = 0; i < H; i++) {
				for(int j = 0; j < W; j++ ) {
					sb.append(graph[i][j]);
				}
				sb.append("\n");
			}
			
			
		}
		System.out.println(sb);
	}
}