# IG Watermark Spec — The Zero

Padrão oficial (Nicholas / CEO, 2026-09-18). Todo criativo novo de Instagram usa isto.
Não retrofit de posts já no ar (ex.: Xbox live).

## Tokens

| Token | Hex |
|---|---|
| bg | `#0A0A0B` |
| fg / wordmark | `#F4F4F5` |
| accent (kicker) | `#7CFFB2` |
| muted (handle / apoio) | `#8B8B93` |

Asset wordmark: `public/brand/logo-on-dark.svg` (fill claro, O partido). Sem quadrado preto.

## Watermark

- **Estilo:** wordmark puro estilo OG do site. Sem pill, sem caixa opaca, sem ring.
- **Scrim:** só se a foto for ocupada — gradiente suave 0→~40% preto no canto do mark. Nunca caixa.
- **Posição padrão:** canto superior direito (como OG de artigo). Alternativa foto-produto: canto inferior direito.
- **Largura do wordmark:** 14–18% da largura do frame (em 1080px ≈ 150–195px).
- **Padding:** 4–5% da menor dimensão (~48–54px em 1080).
- **Handle:** `@hello.the.zero` abaixo do wordmark, `#8B8B93` (ou `#7CFFB2` se precisar de brilho), ~2–2.4% da largura (~22–26px em 1080).
- **Opacidade wordmark:** 90–100% (mín. 85%).

Ferramenta: `tools/ig_brand.py`.

## Tipografia carrossel (mobile-first)

- Canvas preferencial: **1080×1350 (4:5)**; 1080×1080 ok.
- Fundo base: `#0A0A0B`. Gancho: `#F4F4F5`. Kicker: `#7CFFB2`. Apoio: `#8B8B93`.
- **Frame 1 (viral):** 6–12 palavras, bold/semibold (650–800), tamanho 9–12% da altura (~120–160px em 1350), line-height 0.92–1.0, tracking −2% a −4%, máx. 3 linhas.
- Texto sobre foto: sempre gradiente escuro atrás do bloco (contraste legível). Proibido branco em mid-tone sem scrim.
- Slides 2+: corpo 4.5–6% da altura (~60–80px). Máx. 2 ideias/slide. Margem segura **10–12%** das bordas (tipografia e wordmark nunca na zona de crop do IG).
- Hierarquia: kicker mint uppercase tracking largo → gancho gigante → 1 linha apoio muted.

## Checklist de entrega

- [ ] Wordmark O partido + `@hello.the.zero` no canto (spec acima)
- [ ] Frame 1 grita em 1s no celular
- [ ] Sem pill / caixa / watermark genérico
- [ ] Notícia = foto real da fonte; opinião/demo = Flow/Gemini (conta `lavi.id.project@gmail.com`)
- [ ] CEO revisa antes de publicar / trocar post

## Voz nos ganchos e overlays (Nicholas)

Linguagem fácil, humana, anti-robótica. O overlay tem que parecer falado no celular — não relatório de segurança.

- Preferir: “sua extensão pode mandar no Gemini sem você ver”
- Evitar: jargão de CVE, siglas soltas, tom de press release
- Frame 1: conflito concreto + consequência pro usuário, em português do dia a dia
