def calcul_prix(produits, catalogue):
    """Calcul le prix total des produits"""
    # Initialiser le prix total
    prix = 0
    # Parcourir les produits
    for produit, nbr in produits.items():
        # Si le produit est dans le catalogue
        if produit in catalogue:
            # Ajouter le prix du produit au prix total
            prix += nbr * catalogue[produit]
    # Retourner le prix total
    return prix