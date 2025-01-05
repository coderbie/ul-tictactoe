import asyncio
from ul_tictactoe import TicTacToe
import pickle

async def handle_server():
        game_ip = input("Enter the Game IP: ")
        game_port = int(input("Enter the Game Port: "))

        try:
            reader, writer = await asyncio.open_connection(game_ip, game_port)
            game = TicTacToe()

            while True:
                print("You are Player 2.")

                print("Player 1 is playing....")
                data = await recv_chunk(reader)
                data = pickle.loads(data)
                game.move(data[0], data[1])
                game.print_game()
                if game.win_mgmt():
                    writer.close()
                    await writer.wait_closed()
                    break
                    
                print("Your Turn:")
                game.turn()
                game.print_game()

                data = (game.played_larger_cell, game.played_smaller_cell)
                data = pickle.dumps(data)
                await send_chunk(data, writer)
                if game.win_mgmt():
                    writer.close()
                    await writer.wait_closed()
                    break

                if game.moves > 81:
                    print("Draw!")
                    writer.close()
                    await writer.wait_closed()
                    break
        except Exception as e:
            print(f"Error: {e}")
async def recv_chunk(reader):
    prefix = await reader.readline()
    chunk_len = int(prefix)
    return await reader.readexactly(chunk_len)
            
async def send_chunk(content, writer):
    writer.write(b'%d\n' % len(content))
    writer.write(content)
    await writer.drain()

asyncio.run(handle_server())
