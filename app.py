import streamlit as st
import chess.pgn

# Cargar archivo PGN
st.title("Análisis de Datos de Juegos de Ajedrez")
uploaded_file = st.file_uploader("Sube tu partida en formato PGN", type="pgn")

if uploaded_file:
    # Decodifica el archivo BytesIO a texto
    pgn_text = uploaded_file.read().decode("utf-8")
    
    # Cargar la partida desde el texto
    game = chess.pgn.read_game(pgn_text.splitlines(True))
    
    # Mostrar la partida (por ahora, solo los movimientos)
    board = game.board()
    st.write("**Movimientos de la partida:**")
    for move in game.mainline_moves():
        board.push(move)
        st.write(board.fen())  # Opcional: Puedes reemplazar con la visualización de un tablero SVG
