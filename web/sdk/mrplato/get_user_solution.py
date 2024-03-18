

from src._shared.errors.not_found import NotFoundError



def get_solution_service(prover_instance):
    if prover_instance is None:
        raise NotFoundError("prover_instance not found")
    
    solutions = []
    for line in prover_instance.proof_lines:
        solutions.append(f"content: {str(line[0])} methods_used_info: {str(line[1])}")

    return solutions