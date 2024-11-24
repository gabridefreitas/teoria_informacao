import os
import matplotlib.pyplot as plt

# Diretório contendo as imagens
image_dir = "./imgs"
original_image = "look.jpg"  # Nome do arquivo da imagem original
quality_values = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]  # Qualidade em %

# Resultados
file_sizes_kb = []  # Tamanhos das imagens em KB
compression_ratios = []  # Relação de compressão

# Tamanho da imagem original
original_path = os.path.join(image_dir, original_image)
original_size_kb = os.path.getsize(original_path) / 1024  # Convertendo para KB

# Analisando cada imagem comprimida
for quality in quality_values:
    compressed_image = f"look{quality}.jpg"
    compressed_path = os.path.join(image_dir, compressed_image)
    compressed_size_kb = os.path.getsize(compressed_path) / 1024  # Convertendo para KB
    file_sizes_kb.append(compressed_size_kb)
    compression_ratios.append(original_size_kb / compressed_size_kb)

# Adicionando o tamanho da imagem original na lista
quality_values.append(100)
file_sizes_kb.append(original_size_kb)
compression_ratios.append(0)

# Gerando o gráfico com eixo duplo
fig, ax1 = plt.subplots(figsize=(10, 6))

# Eixo esquerdo
ax1.set_xlabel("Qualidade JPEG (%)")
ax1.set_ylabel("Tamanho do Arquivo (KB)", color="blue")
ax1.plot(
    quality_values,
    file_sizes_kb,
    marker="o",
    color="blue",
    label="Tamanho do Arquivo (KB)",
)
ax1.tick_params(axis="y", labelcolor="blue")

# Eixo direito
ax2 = ax1.twinx()
ax2.set_ylabel("Razão de Compressão", color="green")
ax2.plot(
    quality_values,
    compression_ratios,
    marker="s",
    color="green",
    label="Razão de Compressão",
)
ax2.tick_params(axis="y", labelcolor="green")

# Título e layout
plt.title("Análise de Compressão: Tamanho x Qualidade x Compressão")
fig.tight_layout()
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
