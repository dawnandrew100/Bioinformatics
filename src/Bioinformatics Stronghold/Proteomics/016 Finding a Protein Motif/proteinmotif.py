import re
import requests

def main():
    test_sequence_fasta_ids = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]
    input_sequence_fasta_ids = ["P01189_COLI_HUMAN", "P17967", "P03395_ENV_MLVFR", "P19835_BAL_HUMAN", 
                                "P11831_SRF_HUMAN", "Q3BRP8", "P12763_A2HS_BOVIN", "P46096_SYT1_MOUSE", 
                                "A9QYR8", "P01045_KNH2_BOVIN", "P19246_NFH_MOUSE", "P05113_IL5_HUMAN",
                                "Q8ZRE7", "Q5U1Y9"]
    chosen_motif = "N[^P][ST][^P]"

    if not is_valid_response("B5ZC00"):
        raise RuntimeError("Unable to get uniprot data and parse into dictionary")

    uniprot_ids = get_uniprot_fasta(input_sequence_fasta_ids)
    motif_locs = motif_finder(uniprot_ids, chosen_motif)
    for motif, value in motif_locs.items():
        print(f"{motif}\n{" ".join(value)}")

def _uniprot_fasta_parser(fasta: str)-> dict[str, str]:
    """
    :param fasta: raw fasta string
    :return: fasta parsed into name:sequence dictionary
    """
    temp = [x.strip() for x in fasta.split("\n")]
    fast_index = [i for i, j in enumerate(temp) if ">" in j]
    if len(fast_index) == 1:
        title_temp = temp[0].split("|")
        title = title_temp[1]
        return {title:"".join(temp[1:])}
    raise RuntimeError("Failed to parse file due to improper fasta format")

def is_valid_response(fasta: str) -> bool:
    #This function is here just to make sure all the individual steps work as intended
    uniprot_id = fasta
    response = requests.get(f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta")
    test = _uniprot_fasta_parser(response.text)

    if [test[uniprot_id]] == ["MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQ"
                                "KDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSS"
                                "NEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVN"
                                "FKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKY"
                                "LNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYD"
                                "LSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILM"
                                "DLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIY"
                                "CLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK"]:
        return True
    return False #get request unsuccessful or fasta not parsed correctly

def get_uniprot_fasta(fasta_seqs: list[str]) -> dict[str, str]:
    """
    :param fasta_seqs: list of uniprot ids
    :return: dictionary containing items following the format unitprot_id:sequence
    """
    fasta_dict = {}
    for orig_uniprot_id in fasta_seqs:
        uniprot_id = orig_uniprot_id.split("_")[0] #only first section of underscore separated names are valid uniprot IDs
        response = requests.get(f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta")
        parsed = _uniprot_fasta_parser(response.text)
        key, value = list(parsed.items())[0]
        fasta_dict[orig_uniprot_id] = value #Rosalind wants original ID to be returned
    return fasta_dict

def motif_finder(fasta_dict: dict[str, str], pattern: str) -> dict[str, list[str]]:
    """
    :param fasta_dict: dictionary of fasta values from get_uniprot_fasta
    :return: dictionary containing uniprot_id and list of all positions matching motif (including overlapping positions)
    """
    result_dict = {}
    for uniprot_id, value in fasta_dict.items():
        matches = [str(m.start(0)+1) for m in re.finditer(f"(?={pattern})", value)] #positive lookahead match is zero-width
        if matches: #only adds sequences with desired motif to output dictionary
            result_dict[uniprot_id] = matches
    return result_dict

if __name__ == "__main__":
    main()
