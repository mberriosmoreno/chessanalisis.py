import streamlit as st
import chess.pgn
import chess.svg

# Cargar archivo PGN
st.title("Análisis de Datos de Juegos de Ajedrez")
uploaded_file = st.file_uploader("Sube tu partida en formato PGN", type="pgn")

if uploaded_file:
    game = chess.pgn.read_game(uploaded_file)
    board = game.board()

    # Reproducción de la partida
    st.write("**Movimientos de la partida:**")
    for move in game.mainline_moves():
        board.push(move)
        st.write(board.fen())  # Puedes reemplazar con SVG del tablero
