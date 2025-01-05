import asyncio
import pickle
from ul_tictactoe import TicTacToe
import sys

async def handle_client(reader, writer):

    game = TicTacToe()

    try:
        while True:
            print("You are Player 1.")
            game.print_game()

            print("Your Turn:")
            game.turn()
            game.print_game()

            data = (game.played_larger_cell, game.played_smaller_cell)
            data = pickle.dumps(data)
            await send_chunk(data, writer)
            if game.win_mgmt():
                writer.close()
                await writer.wait_closed()
                sys.exit()
                break
            
            print("Player 2 is playing....")

            data = await recv_chunk(reader)
            data = pickle.loads(data)
            game.move(data[0], data[1])
            if game.win_mgmt():
                writer.close()
                await writer.wait_closed()
                sys.exit()
                break
            
            if game.moves > 81:
                print("Draw!")
                writer.close()
                await writer.wait_closed()
                sys.exit()
                break
    except SystemExit:
        print("Game Exited.")
    except Exception as e:
        print(f"Error: {e}")

async def server_player():
    ip = input("Enter the IP: ")
    port = int(input("Enter the Port: "))

    server = await asyncio.start_server(handle_client, ip, port)

    async with server:
        await server.serve_forever()

async def recv_chunk(reader):
    prefix = await reader.readline()
    chunk_len = int(prefix)
    return await reader.readexactly(chunk_len)
            
async def send_chunk(content, writer):
    writer.write(b'%d\n' % len(content))
    writer.write(content)
    await writer.drain()

asyncio.run(server_player())
