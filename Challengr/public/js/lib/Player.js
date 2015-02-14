import { Model } from 'backbone';

export default class Player extends Model {
    constructor(){
        super(...arguments);
    }

    defaults(){
        return {
            type: null,
            owner: null,
            name: null,
            uploaded_at: new Date(),
            wins: 0,
            losses: 0,
            draws: 0,
            games: []
        }
    }
} 