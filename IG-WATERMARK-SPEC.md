# IG Watermark Spec — The Zero

Padrão oficial (Nicholas / CEO). Todo criativo novo de Instagram usa isto.

## Tokens

| Token | Hex |
|---|---|
| bg | `#0A0A0B` |
| fg / wordmark | `#F4F4F5` |
| accent (kicker) | `#7CFFB2` |
| muted (handle / apoio) | `#8B8B93` |

Asset wordmark: `public/brand/logo-on-dark.svg` (fill claro, O partido). Sem quadrado preto.

## Canvas e safe margin

- Canvas padrão: **1080×1080 (1:1)** — Instagram não corta no feed/grid.
- Margem segura: **≥10–12%** em todos os lados. Tipografia e wordmark nunca na zona de crop.

## Watermark

- **Estilo:** wordmark puro estilo OG do site. Sem pill, sem caixa opaca, sem ring.
- **Posição padrão:** canto superior direito. Alternativa foto-produto: canto inferior direito.
- **Largura do wordmark:** ~13–16% da largura do frame.
- **Padding:** ≥10% da menor dimensão.
- **Handle:** `@hello.the.zero` abaixo do wordmark, `#8B8B93` (ou `#7CFFB2` se precisar de brilho).
- **Opacidade wordmark:** 90–100% (mín. 85%).

Ferramenta: `tools/ig_brand.py`.

## Scrim de texto (obrigatório) — Nicholas 2026-09-19

Branco/`#F4F4F5` **só** sobre área já escurecida.

- Em **todo** bloco de texto (kicker, gancho, bullets, CTA, crédito): scrim/gradiente preto atrás.
- Opacidade sob o gancho: **mín. ~55–70% preto** (não 20–30%).
- Preferir `ig_brand.apply_text_scrim()` (`direction=bottom|top|full`) antes de desenhar tipografia.
- Proibido texto claro em foto mid-tone sem scrim.

## Tipografia carrossel

- Fundo base: `#0A0A0B`. Gancho: `#F4F4F5`. Kicker: `#7CFFB2`. Apoio: `#8B8B93`.
- **Frame 1 (viral):** 6–12 palavras, bold, máx. 3 linhas, legível no celular em 1s.
- Slides 2+: máx. 2 ideias/slide.
- Hierarquia: kicker mint → gancho gigante → apoio muted.

## Checklist de entrega

- [ ] 1080×1080 + margem ≥10%
- [ ] Scrim forte sob todo texto (55–70%)
- [ ] Wordmark O partido + `@hello.the.zero`
- [ ] Frame 1 grita em 1s
- [ ] Notícia = foto real; opinião/demo = Flow/Gemini (`lavi.id.project@gmail.com`)
- [ ] CEO revisa antes de publicar / trocar post

## Voz nos ganchos e overlays

Linguagem fácil, humana, anti-robótica. Frases curtas, palavras do dia a dia, opinião clara. Sem jargão de CVE / press release.
