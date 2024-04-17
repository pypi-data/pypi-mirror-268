import argparse
from server_client.start_server_with_ai_client import main as ai_server_main
from server_client.server import main as server_main
from server_client.client import main as client_main
from server_client.terminal_client import main as terminal_client_main

def main():
    parser = argparse.ArgumentParser(description='Run different parts of the chat application.')
    parser.add_argument('--ai', action='store_true', help='Run the AI server.')
    parser.add_argument('--server', action='store_true', help='Run the server.')
    parser.add_argument('--client', action='store_true', help='Run the client.')
    parser.add_argument('--terminal', action='store_true', help='Run the terminal client.')

    # Settings for the AI server
    parser.add_argument('--server_ip_address', type=str, default="127.0.0.1", help='IP address of the server')
    parser.add_argument('--server_port', type=int, default=1234, help='Port number of the server')
    parser.add_argument('--send_full_chat_history', type=lambda x: (str(x).lower() == 'true'), default=True, help='Whether to send full chat history')
    parser.add_argument('--ai_mode1_active', type=lambda x: (str(x).lower() == 'true'), default=True, help='Activate mode 1 AI')
    parser.add_argument('--ai_mode1_interval', type=int, default=1, help='Interval for mode 1 AI responses')
    parser.add_argument('--ai_mode1_model', type=str, default="gpt-3.5-turbo", help='Model for mode 1 AI')
    parser.add_argument('--ai_mode2_active', type=lambda x: (str(x).lower() == 'true'), default=True, help='Activate mode 2 AI')
    parser.add_argument('--ai_mode2_interval', type=int, default=60, help='Interval for mode 2 AI responses')
    parser.add_argument('--ai_mode2_model', type=str, default="gpt-3.5-turbo", help='Model for mode 2 AI')
    parser.add_argument('--ai_mode2_content', type=str, default="Say something interesting from a random Wikipedia page and start your response with 'Did you know', but don't mention the source.", help='Content for mode 2 AI to initiate conversation')

    args = parser.parse_args()

    if args.ai:
        ai_server_main(server_ip_address=args.server_ip_address, server_port=args.server_port,
                       send_full_chat_history=args.send_full_chat_history, ai_mode1_active=args.ai_mode1_active,
                       ai_mode1_interval=args.ai_mode1_interval, ai_mode1_model=args.ai_mode1_model,
                       ai_mode2_active=args.ai_mode2_active, ai_mode2_interval=args.ai_mode2_interval,
                       ai_mode2_model=args.ai_mode2_model, ai_mode2_content=args.ai_mode2_content)
    elif args.server:
        server_main()
    elif args.client:
        client_main()
    elif args.terminal:
        terminal_client_main()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
