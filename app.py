import streamlit as st
import chess.pgn
import io  # Necesario para convertir la cadena en un objeto de archivo

# Título
st.title("Análisis de Datos de Juegos de Ajedrez")

# Subir archivo
uploaded_file = st.file_uploader("Sube tu partida en formato PGN", type="pgn")

if uploaded_file:
    # Decodifica el archivo a texto
    pgn_text = uploaded_file.read().decode("utf-8")

    # Convierte el texto a un objeto de archivo usando StringIO
    pgn_file = io.StringIO(pgn_text)

    # Lee la partida PGN
    game = chess.pgn.read_game(pgn_file)

    # Mostrar información básica de la partida
    if game:
        st.write("**Información del juego:**")
        st.write(f"Blancas: {game.headers['White']}")
        st.write(f"Negras: {game.headers['Black']}")
        st.write(f"Resultado: {game.headers['Result']}")

        # Mostrar movimientos (opcional)
        st.write("**Movimientos de la partida:**")
        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
            st.write(board.fen())  # Puedes reemplazar con una visualización más amigable
