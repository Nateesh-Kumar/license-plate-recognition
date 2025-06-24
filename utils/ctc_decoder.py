from difflib import SequenceMatcher

def ctc_decode(preds, idx_to_char):
    preds_idx = preds.permute(1, 0, 2).argmax(2)  # [B, T]
    decoded = []

    for pred in preds_idx:
        chars = []
        prev = -1
        for p in pred:
            p = p.item()
            if p != prev and p != 0:  # skip blanks and repeats
                chars.append(idx_to_char[p])
            prev = p
        decoded.append(''.join(chars))

    return decoded

def char_accuracy(a, b):
    return SequenceMatcher(None, a, b).ratio()