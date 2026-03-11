def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    
    # intersection = [i for i in recommended if i in relevant]
    # precision_at_k = len(intersection) / k
    # recall_at_k = len(intersection) / len(relevant)

    recommended_k = recommended[:k]
    relevant = set(relevant)

    hits = len(set(recommended_k) & relevant)

    precision_at_k = hits / k if k > 0 else 0
    recall_at_k = hits / len(relevant) if len(relevant) > 0 else 0
    
    return [precision_at_k, recall_at_k]
